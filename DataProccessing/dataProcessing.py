from DataProccessing.processingImports import *

def splitCounsellors(counsellors, activities):
    cabins = {}
    specialists = {}
    for i in range(len(activities)):
        specialists[activities[i]] = []
    for counsellor in counsellors:
        for i in range(len(activities)):
            if counsellor[3] == activities[i]:
                specialists.update({activities[i]: specialists[activities[i]] + [counsellor[0]]})

    cabinNums = findCabins()

    for i in range(len(cabinNums)):
        cabins[cabinNums[i]] = []
    for counsellor in counsellors:
        for i in range(len(cabinNums)):
            if counsellor[2] == cabinNums[i]:
                cabins.update({cabinNums[i]: cabins[cabinNums[i]] + [counsellor[0]]})

    return cabins, specialists


def splitInstructors(instructors, activities):
    instructorDict = {}
    for i in range(len(activities)):
        instructorDict[activities[i]] = []
    for instructor in instructors:
        for i in range(len(activities)):
            if instructor[1] == activities[i]:
                instructorDict.update({activities[i]: instructorDict[activities[i]] + [[instructor[0], instructor[2]]]})

    return instructorDict


def getExclusions(name, counsellorDict, specialistDict, instructorDict, PDs, PDActivities, HCs, SHs):
    master_list = mutualExclusions()
    individual_list = []
    for element in master_list:
        if element[0] == name:
            individual_list.append(element[1])
        if element[1] == name:
            individual_list.append(element[0])

    # CO COUNSELLORS
    counsellors = list(counsellorDict.values())
    cabins = list(counsellorDict.keys())
    index = -1
    for cabin in counsellors:
        for counsellor in cabin:
            if counsellor == name:
                index = counsellors.index(cabin)
                break

    if not (index == -1):
        cabinNum = cabins[index]
        cocounsellors = []
        for element in counsellorDict[cabinNum]:
            cocounsellors.append(element)
        cocounsellors.remove(name)
        if len(cocounsellors) >= 3:
           cocounsellors = cocounsellors[0:(len(cocounsellors)-1)]
        for staff in cocounsellors:
            individual_list.append(staff)

    # SPECIALISTS
    specialists = list(specialistDict.values())
    activities = list(specialistDict.keys())
    index = -1
    for activity in specialists:
        for specialist in activity:
            if specialist == name:
                index = specialists.index(activity)
                break

    if not (index == -1):
        activity = activities[index]
        cospecialists = []
        for element in specialistDict[activity]:
            cospecialists.append(element)
        cospecialists.remove(name)
        while len(cospecialists) >= 4:
            rand_specialist = random.choice(cospecialists)
            cospecialists.remove(rand_specialist)  # Multiple specialists on the same day off
        for staff in cospecialists:
            individual_list.append(staff)
        activityStaff = instructorDict[activity]

        for staff in activityStaff:
            if staff[1] == "H":
                individual_list.append(staff[0])

        individual_list = list(dict.fromkeys(individual_list))  # Remove duplicates
        return individual_list

    # HEAD/ASSISTANT/CO-HEADS
    instructors = list(instructorDict.values())
    activities = list(instructorDict.keys())
    index = -1
    position = "NULL"
    for activity in instructors:
        for instructor in activity:
            if instructor[0] == name:
                index = instructors.index(activity)
                position = instructor[1]
                break

    if not (index == -1):
        activity = activities[index]
        staff = []

        for element in instructorDict[activity]:
            staff.append(element[0])
        staff.remove(name)
        for staffLoop in staff:
            individual_list.append(staffLoop)

        if position == "H":
            for PD in range(len(PDs)):
                if activity in PDActivities[PD]:
                    individual_list.append(PDs[PD][0])
        elif position == "CO" or position == "A":
            pass
        else:
            print("ERROR: " + position + " is not a valid position for " + name)
            popup("ERROR", position + " is not a valid position for " + name)

    # PDs
    activityHeadInstructor = list()
    for activity in instructors:
        for instructor in activity:
            if instructor[1] == 'H':
                index = instructors.index(activity)
                activityHeadInstructor.append([activities[index], instructor[0]])
    for PD in range(len(PDs)):
        if PDs[PD][0] == name:
            for otherPDs in PDs:
                if not name == otherPDs[0]:
                    individual_list.append(otherPDs[0])
            PDActivities = PDActivities[PD]
            for activityInstructor in activityHeadInstructor:
                if activityInstructor[0] in PDActivities:
                    individual_list.append(activityInstructor[1])

    # Head Counsellor + SH
    for HC in HCs:
        if name == HC[0]:
            HCsections = HC[1:4]
            for section in HCsections:
                for i in range(len(SHs)):
                    if section == SHs[i][0]:
                        individual_list.append(SHs[i][1])
    for SH in SHs:
        if name == SH[1]:
            # SH-SH
            if "LIT" not in SH[0]:  # If not LIT
                for otherSHs in SHs:
                    if not name == otherSHs[1] and not "LIT" in otherSHs[0]:
                        individual_list.append(otherSHs[1])
            else:
                for otherSHs in SHs:  # If LIT
                    if not name == otherSHs[1] and "LIT" in otherSHs[0]:
                        individual_list.append(otherSHs[1])
            # SH-HC
            for HC in HCs:
                if SH[0] in HC:
                    individual_list.append(HC[0])

    individual_list = list(dict.fromkeys(individual_list))  # Remove duplicates
    return individual_list


def getTag(name, specialistDict, instructorDict, pds, shs, hcs):
    for pd in pds:
        if pd[0] == name:
            return "PD"
    for sh in shs:
        if sh[1] == name:
            return sh[0]
    for hc in hcs:
        if hc[0] == name:
            return f"{hc[1]}/{hc[2]}"
    for activity, nameArray in instructorDict.items():
        for instructor in nameArray:
            if instructor[0] == name:
                return activity
    for activity, nameArray in specialistDict.items():
        for counsellor in nameArray:
            if counsellor == name:
                return activity
    return "N/A"


def findCycleOverlap(day1, day2):
    secondlastday, lastday = findLastCycle()
    finalArray = []
    for name in secondlastday:
        finalArray.append([name, day1])
        finalArray.append([name, day2])
    for name in lastday:
        finalArray.append([name, day1])
        finalArray.append([name, day2])
    return finalArray