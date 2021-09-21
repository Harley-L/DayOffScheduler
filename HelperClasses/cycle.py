from HelperClasses.classImports import *


class Cycle:
    def __init__(self, numdays, startDate):
        self.date_range = []
        self.date_range_string = []
        for i in range(numdays):
            self.date_range.append(Date(startDate + datetime.timedelta(days=i)))
        for element in self.date_range:
            self.date_range_string.append(element.toString())
        self.days = []
        for day in range(numdays):
            self.days.append([])

        self.errors = []
        self.overlap48Hrs = findCycleOverlap(self.date_range_string[0], self.date_range_string[1])

        self.counsellors = findCounsellors()
        self.PDs, self.PDActivities = findPDs()
        self.instructors = findInstructors()
        self.section_heads, self.head_counsellors = findHeadStaff()
        self.activities = findActivities()
        self.counsellorDict, self.specialistDict = splitCounsellors(self.counsellors, self.activities)
        self.instructorDict = splitInstructors(self.instructors, self.activities)

        self.PDMustNotDate, self.HCMustNotDate, self.InstructorMustNotDate, self.SHMustNotDate, self.CounsellorMustNotDate = findMustNotDate(
            self.PDs, self.head_counsellors, self.instructors, self.section_heads, self.counsellors)
        self.must_not_dates = self.PDMustNotDate + self.HCMustNotDate + self.SHMustNotDate + self.CounsellorMustNotDate + \
                              self.InstructorMustNotDate + self.overlap48Hrs

        self.PDReqDate, self.HCReqDate, self.InstructorReqDate, self.SHReqDate, self.CounsellorReqDate = findReqDate(
            self.PDs,
            self.head_counsellors,
            self.instructors,
            self.section_heads,
            self.counsellors)

        self.dualMustRequirements = findDualMustRequirements()
        self.masterMustNot = {}
        self.masterExclusions = {}

    def appendToDay(self, name, date, must_not_dates):  # ONLY APPENDS IF THE DATE IS IN THE CYCLE AND IF NO CONFLICTS
        exclusions = getExclusions(name, self.counsellorDict, self.specialistDict, self.instructorDict, self.PDs,
                                   self.PDActivities, self.head_counsellors, self.section_heads)

        bad_dates = []
        for must_not_date in must_not_dates:
            if must_not_date[0] == name:
                bad_dates.append((must_not_date[1]))

        for i in range(len(self.days)):
            if date == self.date_range_string[i]:
                if date in bad_dates:
                    raise SameDayMustMustNotError(name, date)
                for placedStaff in self.days[i]:
                    if placedStaff in exclusions:
                        raise TwoStaffConflict(name, placedStaff)
                self.days[i].append(name)

    def inputMusts(self):
        # PDs
        for i in range(len(self.PDReqDate)):
            if self.PDReqDate[i][1] in self.date_range_string:
                self.appendToDay(self.PDReqDate[i][0], self.PDReqDate[i][1], self.must_not_dates)
        # HCs
        for i in range(len(self.HCReqDate)):
            if self.HCReqDate[i][1] in self.date_range_string:
                self.appendToDay(self.HCReqDate[i][0], self.HCReqDate[i][1], self.must_not_dates)
        # Instructors
        for i in range(len(self.InstructorReqDate)):
            if self.InstructorReqDate[i][1] in self.date_range_string:
                self.appendToDay(self.InstructorReqDate[i][0], self.InstructorReqDate[i][1], self.must_not_dates)
        # SHs
        for i in range(len(self.SHReqDate)):
            if self.SHReqDate[i][1] in self.date_range_string:
                self.appendToDay(self.SHReqDate[i][0], self.SHReqDate[i][1], self.must_not_dates)
        # Counsellors
        for i in range(len(self.CounsellorReqDate)):
            if self.CounsellorReqDate[i][1] in self.date_range_string:
                self.appendToDay(self.CounsellorReqDate[i][0], self.CounsellorReqDate[i][1], self.must_not_dates)

    def checkIfPlaced(self, name):
        for i in range(len(self.days)):
            for element in self.days[i]:
                if name == element:
                    return True
        return False

    def dispCycle(self):
        print(f"Cycle:")
        for i in range(len(self.days)):
            print(f"Day {i + 1} (" + self.date_range_string[i] + "): ", end='')
            for name in self.days[i]:
                tag = getTag(name, self.specialistDict, self.instructorDict, self.PDs, self.section_heads,
                             self.head_counsellors)
                print(name + ": " + tag + ", ", end='')
            print("")

        print("Could not find a day off for: " + str(self.errors))

    def showErrors(self):
        for staff in self.errors:
            print(f"\n{staff} Conflicts:")
            for i in range(len(self.date_range_string)):
                print(f"Day {i + 1}({self.date_range_string[i]}): ")
                if self.date_range_string[i] in self.masterMustNot[staff]:
                    print(f"Manually said {staff} cannot be on this day off")

                if not self.masterExclusions[staff][i] == []:
                    print(
                        f"These staff are on this day off and {staff} cannot be with them: {self.masterExclusions[staff][i]}")

    def inputDuals(self):
        for pair in self.dualMustRequirements:
            exclusions = getExclusions(pair[0], self.counsellorDict, self.specialistDict, self.instructorDict, self.PDs,
                                       self.PDActivities, self.head_counsellors, self.section_heads)
            if pair[1] in exclusions:
                raise TwoStaffConflict(pair[0], pair[1])
            # Three situations:
            numPlaced = 0
            for i in range(len(self.days)):
                if pair[0] in self.days[i]:
                    numPlaced += 1
                if pair[1] in self.days[i]:
                    numPlaced += 1
            print(pair[0], pair[1])
            # Both of the names are present (On the same day(do nothing) OR on two different days(report error))
            if numPlaced == 2:
                for i in range(len(self.days)):
                    if pair[0] in self.days[i] and pair[1] in self.days[i]:
                        break
                    elif pair[0] in self.days[i] or pair[1] in self.days[i]:
                        raise TwoStaffConflict(pair[0], pair[1])
            # One of the name is present (check if other can go on same day and either put it or display error)
            elif numPlaced == 1:
                for i in range(len(self.days)):
                    if pair[0] in self.days[i] or pair[1] in self.days[i]:
                        # Which is placed?
                        if pair[0] in self.days[i]:
                            if self.checkPlaceable(pair[1], self.date_range_string[i], self.days[i]):
                                self.days[i].append(pair[1])
                            else:
                                raise TwoStaffConflict(pair[0], pair[1])
                        elif pair[1] in self.days[i]:
                            if self.checkPlaceable(pair[0], self.date_range_string[i], self.days[i]):
                                self.days[i].append(pair[0])
                            else:
                                raise TwoStaffConflict(pair[0], pair[1])

            else:
                possibleDays = []
                numPerDay = []
                for i in range(len(self.days)):
                    if self.checkPlaceable(pair[0], self.date_range_string[i], self.days[i]) and \
                            self.checkPlaceable(pair[1], self.date_range_string[i], self.days[i]):
                        possibleDays.append(self.days[i])
                        numPerDay.append(len(self.days[i]))
                if len(possibleDays) == 0:
                    raise TwoStaffConflict(pair[0], pair[1])
                # find the lowest # of people on it...
                indexes = []
                for i in range(len(numPerDay)):
                    if numPerDay[i] == min(numPerDay):
                        indexes.append(i)
                # If multiple days with the lowest # of ppl use random to pick one
                choice = random.choice(indexes)
                possibleDays[choice].append(pair[0])
                possibleDays[choice].append(pair[1])

    def checkPlaceable(self, name, dateStr, day):
        exclusions = getExclusions(name, self.counsellorDict, self.specialistDict, self.instructorDict, self.PDs,
                                   self.PDActivities, self.head_counsellors, self.section_heads)
        for exclusion in exclusions:
            if exclusion in day:
                return False

        bad_dates = []
        for must_not_date in self.must_not_dates:
            if must_not_date[0] == name:
                bad_dates.append((must_not_date[1]))
        if dateStr in bad_dates:
            return False
        return True

    def buildCycle(self):
        self.inputMusts()
        self.inputDuals()
        self.placeStaff(self.PDs, 0, self.must_not_dates, "Program Directors")
        self.placeStaff(self.head_counsellors, 0, self.must_not_dates, "Head Counsellors")
        self.placeStaff(self.instructors, 0, self.must_not_dates, "Instructors")
        self.placeStaff(self.section_heads, 1, self.must_not_dates, "Section Heads")
        self.placeStaff(self.counsellors, 0, self.must_not_dates, "Counsellors")

    def placeStaff(self, staffType, namePosition, mustNotDate, name):
        print(name + "(" + str(len(staffType)) + "): ", end=' ')
        for staff in staffType:
            print(staffType.index(staff) + 1, end="")
            # Check if placed...
            if self.checkIfPlaced(staff[namePosition]):
                continue

            # find dates it can not be on
            badDates = []
            for element in mustNotDate:
                if element[0] == staff[namePosition]:
                    badDates.append(element[1])
            self.masterMustNot[staff[namePosition]] = badDates

            # compare with dates of rotation and find dates they can be on
            goodDays = []
            for element in self.date_range_string:
                goodDays.append(element)

            for elementB in badDates:
                if elementB in goodDays:
                    goodDays.remove(elementB)

            # Check if mutually exclusive with another staff member
            exclusions = getExclusions(staff[namePosition], self.counsellorDict, self.specialistDict,
                                       self.instructorDict, self.PDs, self.PDActivities, self.head_counsellors,
                                       self.section_heads)
            daysAllowed = []
            numPerDay = []
            self.masterExclusions[staff[namePosition]] = [[], [], [], [], [], [], [], [], [], [], [], [], [], [], [],
                                                          [], [], [], [], [], [], [], [], [], [], [], [], []]

            for i in range(len(self.days)):
                if self.date_range_string[i] in goodDays:
                    allowed = True
                    for name in self.days[i]:
                        if name in exclusions:
                            self.masterExclusions[staff[namePosition]][i].append(name)
                            allowed = False
                    if allowed:
                        daysAllowed.append(self.days[i])
                        numPerDay.append(len(self.days[i]))

            if len(daysAllowed) == 0:
                print("(WARNING: Could not find a day off for " + staff[namePosition] + ")", end="")
                self.errors.append(staff[namePosition])
                print(" ", end="")
                continue
            # find the lowest # of people on it...
            indexes = []
            for i in range(len(numPerDay)):
                if numPerDay[i] == min(numPerDay):
                    indexes.append(i)
            # If multiple days with the lowest # of ppl use random to pick one
            choice = random.choice(indexes)
            daysAllowed[choice].append(staff[namePosition])
            print(" ", end="")
        print("\n")

    def outputExcel(self):
        if os.name == 'nt':
            project_dir = os.getcwd() + '\\Spreadsheets\\output.xlsx'
        else:
            project_dir = get_mac_directory() + '/Spreadsheets/output.xlsx'
        workbook = xlsxwriter.Workbook(project_dir)
        worksheet = workbook.add_worksheet()

        bold_format = workbook.add_format({'bold': 1})
        merge_format = workbook.add_format({'align': 'center', 'bold': 1})
        for i in range(len(self.days)):
            worksheet.merge_range(f'{chr((i * 2) + 65)}1:{chr((i * 2) + 66)}1',
                                  f'Day {1 + i}({self.date_range_string[i]})', merge_format)

        for i in range(len(self.days)):
            worksheet.set_column(i * 2, i * 2, 20)
            worksheet.set_column(1 + (i * 2), 1 + (i * 2), 10)

        for i in range(len(self.days)):
            row = 1
            col = i * 2
            taglist = []
            for name in self.days[i]:
                taglist.append([getTag(name, self.specialistDict, self.instructorDict, self.PDs, self.section_heads,
                                       self.head_counsellors), name])
            first = lambda x: x[0]
            taglist_sorted = sorted(taglist, key=first)
            temp_sorted = [(index, item, [j[1] for j in group]) for index, (item, group) in
                           enumerate(itertools.groupby(taglist_sorted, first), 1)]
            final_array_name = []
            final_array_activity = []
            for item in temp_sorted:
                for name in item[2]:
                    final_array_name.append(name)
                    final_array_activity.append(item[1])
            for i in range(len(final_array_name)):
                worksheet.write_string(row, col, final_array_name[i])
                worksheet.write_string(row, col + 1, final_array_activity[i])
                row += 1

        conflict_messages = []
        for staff in self.errors:
            conflict_messages.append(f"{staff} Conflicts:")
            for i in range(len(self.date_range_string)):
                conflict_messages.append(f"Day {i + 1}({self.date_range_string[i]}): ")
                if self.date_range_string[i] in self.masterMustNot[staff]:
                    conflict_messages.append(f"Manually said {staff} cannot be on this day off")

                if not self.masterExclusions[staff][i] == []:
                    conflict_messages.append(
                        f"These staff are on this day off and {staff} cannot be with them: {self.masterExclusions[staff][i]}")
            conflict_messages.append("")

        day_lengths = []
        for day in self.days:
            day_lengths.append(len(day))
        maxdaylength = max(day_lengths)

        for i in range(len(conflict_messages)):
            worksheet.write_string(maxdaylength + 4 + i, 0, conflict_messages[i])

        while True:
            try:
                workbook.close()
            except xlsxwriter.exceptions.FileCreateError as e:
                # For Python 3 use input() instead of raw_input().
                decision = input("Exception caught in workbook.close(): %s\n"
                                     "Please close the file if it is open in Excel.\n"
                                     "Try to write file again? [Y/n]: " % e)
                if decision != 'n':
                    continue

            break
