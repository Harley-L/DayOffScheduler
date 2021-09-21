from tkinter import *
import os
import shutil
import getpass
from tkinter import filedialog as fd
import os.path
from pathlib import Path
global start_date_global, num_days_global, spreadsheet_global
from sys import platform
if os.name == 'nt':
    import winreg
import sys

def get_mac_directory():
    project_path = os.path.sep.join(sys.argv[0].split(os.path.sep)[:-1])
    if project_path[-15:] == "/Contents/MacOS":
        project_path = project_path[:-15]
        i = -1
        while not (project_path[i] == '/' or project_path[i] == '\\'):
            i -= 1
        project_path = project_path[:i]
    return str(project_path)
