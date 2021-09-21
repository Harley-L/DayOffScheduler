import os
import pandas as pd
import openpyxl
import xlrd
import sys
from HelperClasses.date import *
from GUI.guiImports import *


def readSheet(sheet):
    if os.name == 'nt':
        path = os.getcwd() + "/Spreadsheets/CampDoffSchedule.xlsx"
    else:
        path = get_mac_directory() + "/Spreadsheets/CampDoffSchedule.xlsx"

    xls = pd.ExcelFile(path, engine='openpyxl')

    if sheet == "CounsellorSheet":
        return pd.read_excel(xls, 'Counsellor')
    if sheet == "InstructorSheet":
        return pd.read_excel(xls, 'Instructors')
    if sheet == "DependenciesSheet":
        return pd.read_excel(xls, 'Dependencies')
    if sheet == "CabinActivitySheet":
        return pd.read_excel(xls, 'Cabin+Activity')
    if sheet == "SeniorStaffSheet":
        return pd.read_excel(xls, 'Senior Staff')
    if sheet == "PrevCycleSheet":
        return pd.read_excel(xls, 'Previous Cycle')
    print("ERROR UNKNOWN SHEET")
    return None
