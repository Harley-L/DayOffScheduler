from ExcelReader.readerImports import *

def findPDs():
    SeniorStaffSheet = readSheet("SeniorStaffSheet")
    numPDs =0
    for k in range(1, 4):
        if str(SeniorStaffSheet.iloc[k][11]) != "nan":
            numPDs += 1
            if k == 1:
                PD1 = list()
                PD1.append(str(SeniorStaffSheet.iloc[k][11]))
                for j in range(1, 6):
                    PD1.append(str(SeniorStaffSheet.iloc[k][j+31]))
                PD1Activities = list()
                i=0
                while str(SeniorStaffSheet.iloc[k][12+i]) != "nan":
                    PD1Activities.append(str(SeniorStaffSheet.iloc[k][12+i]))
                    i += 1
            elif k == 2:
                PD2 = list()
                PD2.append(str(SeniorStaffSheet.iloc[k][11]))
                for j in range(1, 6):
                    PD2.append(str(SeniorStaffSheet.iloc[k][j + 31]))
                PD2Activities = list()
                i = 0
                while str(SeniorStaffSheet.iloc[k][12 + i]) != "nan":
                    PD2Activities.append(str(SeniorStaffSheet.iloc[k][12 + i]))
                    i += 1
            elif k == 3:
                PD3 = list()
                PD3.append(str(SeniorStaffSheet.iloc[k][11]))
                for j in range(1, 6):
                    PD3.append(str(SeniorStaffSheet.iloc[k][j + 31]))
                PD3Activities = list()
                i = 0
                while str(SeniorStaffSheet.iloc[k][12 + i]) != "nan":
                    PD3Activities.append(str(SeniorStaffSheet.iloc[k][12 + i]))
                    i += 1
    PDs = []
    PDActivities = []
    if numPDs == 1:
        PDs.append(PD1)
        PDActivities.append(PD1Activities)
    elif numPDs == 2:
        PDs.append(PD1)
        PDActivities.append(PD1Activities)
        PDs.append(PD2)
        PDActivities.append(PD2Activities)
    elif numPDs == 3:
        PDs.append(PD1)
        PDActivities.append(PD1Activities)
        PDs.append(PD2)
        PDActivities.append(PD2Activities)
        PDs.append(PD3)
        PDActivities.append(PD3Activities)

    return PDs, PDActivities


def findCounsellors():
    CounsellorSheet = readSheet("CounsellorSheet")
    i=0
    counsellors = list()
    while str(CounsellorSheet.iloc[i][0]) != "nan":
        Cname = str(CounsellorSheet.iloc[i][0])
        CSection = str(CounsellorSheet.iloc[i][1])
        CCabin = str(CounsellorSheet.iloc[i][2])
        CActivity = str(CounsellorSheet.iloc[i][3])
        # CSpecialist = str(CounsellorSheet.iloc[i][4])
        CTripStart = str(CounsellorSheet.iloc[i][4])
        CTripEnd = str(CounsellorSheet.iloc[i][5])
        CMustNot1 = str(CounsellorSheet.iloc[i][6])
        CMustNot2 = str(CounsellorSheet.iloc[i][7])
        CMustNot3 = str(CounsellorSheet.iloc[i][8])
        CMustNot4 = str(CounsellorSheet.iloc[i][9])
        CMustGo = str(CounsellorSheet.iloc[i][10])

        CtempArray = [Cname, CSection, CCabin, CActivity, "", CTripStart, CTripEnd, CMustNot1, CMustNot2,
                      CMustNot3, CMustNot4, CMustGo]
        counsellors.append(CtempArray)

        i += 1

    return counsellors


def findInstructors():
    InstructorSheet = readSheet("InstructorSheet")
    i = 0
    instructors = list()
    while str(InstructorSheet.iloc[i][0]) != "nan":
        Iname = str(InstructorSheet.iloc[i][0])
        IActivity = str(InstructorSheet.iloc[i][1])
        IPosition = str(InstructorSheet.iloc[i][2])
        IMustNot1 = str(InstructorSheet.iloc[i][3])
        IMustNot2 = str(InstructorSheet.iloc[i][4])
        IMustNot3 = str(InstructorSheet.iloc[i][5])
        IMustNot4 = str(InstructorSheet.iloc[i][6])
        IMustGo = str(InstructorSheet.iloc[i][7])

        CtempArray = [Iname, IActivity, IPosition, IMustNot1, IMustNot2, IMustNot3, IMustNot4, IMustNot2, IMustGo]
        instructors.append(CtempArray)

        i += 1

    return instructors


def findHeadStaff():
    SeniorStaffSheet = readSheet("SeniorStaffSheet")
    i = 1
    sh = list()
    while str(SeniorStaffSheet.iloc[i][3]) != "nan":
        SHSection = str(SeniorStaffSheet.iloc[i][3])
        SHName = str(SeniorStaffSheet.iloc[i][4])
        SHMustNot1 = str(SeniorStaffSheet.iloc[i][5])
        SHMustNot2 = str(SeniorStaffSheet.iloc[i][6])
        SHMustNot3 = str(SeniorStaffSheet.iloc[i][7])
        SHMustNot4 = str(SeniorStaffSheet.iloc[i][8])
        SHMustGo = str(SeniorStaffSheet.iloc[i][9])
        CtempArray = [SHSection, SHName, SHMustNot1, SHMustNot2, SHMustNot3, SHMustNot4, SHMustGo]
        sh.append(CtempArray)

        i += 1

    hc = list()
    HCCount = 0
    for i in range(12, 15):
        try:
            if str(SeniorStaffSheet.iloc[i][4]) == "nan":
                break
        except:
            break
        HCName = str(SeniorStaffSheet.iloc[i][4])
        HCSection1 = str(SeniorStaffSheet.iloc[i][5])
        HCSection2 = str(SeniorStaffSheet.iloc[i][6])
        HCSection3 = str(SeniorStaffSheet.iloc[i][7])
        HCMustNot1 = str(SeniorStaffSheet.iloc[i][8])
        HCMustNot2 = str(SeniorStaffSheet.iloc[i][9])
        HCMustNot3 = str(SeniorStaffSheet.iloc[i][10])
        HCMustNot4 = str(SeniorStaffSheet.iloc[i][11])
        HCMustGo = str(SeniorStaffSheet.iloc[i][12])
        CtempArray = [HCName, HCSection1, HCSection2, HCSection3, HCMustNot1, HCMustNot2, HCMustNot3, HCMustNot4,
                      HCMustGo]
        hc.append(CtempArray)
        HCCount += 1
    return sh, hc


def findActivities():
    CabinActivitySheet = readSheet("CabinActivitySheet")
    activities = list()
    i=0
    while str(CabinActivitySheet.iloc[i][6]) != "nan":
        activities.append(str(CabinActivitySheet.iloc[i][6]))
        i += 1
    return activities


def findCabins():
    CabinActivitySheet = readSheet("CabinActivitySheet")
    cabins = list()
    i = 0
    while str(CabinActivitySheet.iloc[i][1]) != "nan":
        cabins.append(str(CabinActivitySheet.iloc[i][1]))
        i += 1

    return cabins
