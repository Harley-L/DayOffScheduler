from DataProccessing.processingImports import *

def findReqDate(PDs, HCs, Instructors, SHs, Counsellors):
    PDReqDate = []
    HCReqDate = []
    InstructorReqDate = []
    SHReqDate = []
    CounsellorReqDate = []

    for i in range(len(PDs)):
        if not checkIfEmpty(PDs[i][5]):
            PDReqDate.append([PDs[i][0], convertToDate(str(PDs[i][5])).toString()])

    for i in range(len(HCs)):
        if not checkIfEmpty(HCs[i][7]):
            HCReqDate.append([HCs[i][0], convertToDate(str(HCs[i][7])).toString()])

    for i in range(len(Instructors)):
        if not checkIfEmpty(Instructors[i][8]):
            InstructorReqDate.append([Instructors[i][0], convertToDate(str(Instructors[i][8])).toString()])

    for i in range(len(SHs)):
        if not checkIfEmpty(SHs[i][6]):
            SHReqDate.append([SHs[i][1], convertToDate(str(SHs[i][6])).toString()])

    for i in range(len(Counsellors)):
        if not checkIfEmpty(Counsellors[i][11]):
            CounsellorReqDate.append([Counsellors[i][0], convertToDate(str(Counsellors[i][11])).toString()])

    # HCReqDate =
    # InstructorReqDate =
    # SHReqDate =
    # CounsellorReqDate =

    return PDReqDate, HCReqDate, InstructorReqDate, SHReqDate, CounsellorReqDate


def findMustNotDate(PDs, HCs, Instructors, SHs, Counsellors):
    PDMustNotDate = []
    HCMustNotDate = []
    InstructorMustNotDate = []
    SHMustNotDate = []
    CounsellorMustNotDate = []

    # Add must not dates Program Directors
    for i in range(len(PDs)):
        for j in range(4):
            if not checkIfEmpty(PDs[i][j+1]):
                PDMustNotDate.append([PDs[i][0], convertToDate(str(PDs[i][j+1])).toString()])

    # Add must not dates Head counsellors
    for i in range(len(HCs)):
        for j in range(4):
            if not checkIfEmpty(HCs[i][j + 4]):
                HCMustNotDate.append([HCs[i][0], convertToDate(str(HCs[i][j + 3])).toString()])

    # Add must not dates Instructors
    for i in range(len(Instructors)):
        for j in range(4):
            if not checkIfEmpty(Instructors[i][j + 3]):
                InstructorMustNotDate.append([Instructors[i][0], convertToDate(str(Instructors[i][j + 3])).toString()])

    # Add must not dates Section Heads
    for i in range(len(SHs)):
        for j in range(4):
            if not checkIfEmpty(SHs[i][j + 2]):
                SHMustNotDate.append([SHs[i][1], convertToDate(str(SHs[i][j + 2])).toString()])

    # Add must not dates Counsellors
    for i in range(len(Counsellors)):
        for j in range(4):
            if not checkIfEmpty(Counsellors[i][j + 7]):
                CounsellorMustNotDate.append([Counsellors[i][0], convertToDate(str(Counsellors[i][j + 7])).toString()])
        # Trip
        if not checkIfEmpty(Counsellors[i][5]):
            tripDates = getTripDates(Counsellors[i][5], Counsellors[i][6])
            for tripDate in tripDates:
                CounsellorMustNotDate.append([Counsellors[i][0], tripDate.toString()])

    return PDMustNotDate, HCMustNotDate, InstructorMustNotDate, SHMustNotDate, CounsellorMustNotDate


def getTripDates(startDate, endDate):
    tripDays = []
    if checkIfEmpty(startDate) or checkIfEmpty(endDate):
        return tripDays
    startDate = convertToDate(startDate)
    endDate = convertToDate(endDate)

    sdate = date(startDate.year, startDate.month, startDate.day)  # start date
    edate = date(endDate.year, endDate.month, endDate.day)  # end date

    delta = edate - sdate  # as timedelta

    for i in range(delta.days + 0):
        day = sdate + timedelta(days=i-0)
        if day.month < 10 and day.day < 10:
            stringDay = str(day.year) + "-0" + str(day.month) + "-0" + str(day.day)
        elif day.month < 10:
            stringDay = str(day.year) + "-0" + str(day.month) + "-" + str(day.day)
        elif day.day < 10:
            stringDay = str(day.year) + "-" + str(day.month) + "-0" + str(day.day)
        else:
            stringDay = str(day.year) + "-" + str(day.month) + "-" + str(day.day)
        tripDays.append(convertToDate(stringDay))

    return tripDays


def isDateError(name, mustDate, mustNotDates):
    print(name, mustDate.toString(), mustNotDates.toString())