from ExcelReader.readerImports import *

def countPDs():
    SeniorStaffSheet = readSheet("SeniorStaffSheet")
    numPD = 0
    if not checkIfEmpty(SeniorStaffSheet.iloc[1][11]):
        numPD += 1
    if not checkIfEmpty(SeniorStaffSheet.iloc[2][11]):
        numPD += 1
    if not checkIfEmpty(SeniorStaffSheet.iloc[3][11]):
        numPD += 1
    return numPD

def mutualExclusions():
    DependenciesSheet = readSheet("DependenciesSheet")
    exclusions = []

    for i in range(148):
        try:
            if str(DependenciesSheet.iloc[i+1][12]) == "nan" or str(DependenciesSheet.iloc[i+1][13]) == "nan":
                continue
            person1 = str(DependenciesSheet.iloc[i+1][12])
            person2 = str(DependenciesSheet.iloc[i+1][13])
            exclusions.append([person1, person2])
        except:
            pass
    return exclusions


def findDualMustRequirements():
    DependenciesSheet = readSheet("DependenciesSheet")
    duelMustRequirements = []

    for i in range(148):
        try:
            if str(DependenciesSheet.iloc[i+1][16]) == "nan" or str(DependenciesSheet.iloc[i+1][13]) == "nan":
                continue
            person1 = str(DependenciesSheet.iloc[i+1][16])
            person2 = str(DependenciesSheet.iloc[i+1][17])
            duelMustRequirements.append([person1, person2])
        except:
            pass
    return duelMustRequirements



def checkIfEmpty(cell):
    cell = str(cell)
    if cell == "nan" or cell.isspace() or cell == "None":
        return True
    return False

def findLastCycle():
    PrevCycleSheet = readSheet("PrevCycleSheet")
    secondlastday = []
    lastday = []
    for i in range(148):
        try:
            if str(PrevCycleSheet.iloc[i + 1][2]) == "nan":
                continue
            secondlastday.append(str(PrevCycleSheet.iloc[i + 1][2]))
        except:
            pass
    for i in range(148):
        try:
            if str(PrevCycleSheet.iloc[i + 1][3]) == "nan":
                continue
            lastday.append(str(PrevCycleSheet.iloc[i + 1][3]))
        except:
            pass
    return secondlastday, lastday
