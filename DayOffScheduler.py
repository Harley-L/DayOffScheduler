# Imports
from tkinter import *
from GUI.guiHelperFunctions import *
from HelperClasses.cycle import *
from HelperClasses.date import *
from DataProccessing.dataProcessing import *
from DataProccessing.importantDates import *
from ExcelReader.findStaff import *
from ExcelReader.otherReaders import *
from datetime import datetime
import threading
import traceback

global start_date_global, num_days_global, spreadsheet_global


def updateGlobalVariables():
    global start_date_global, num_days_global, spreadsheet_global
    start_date_global, num_days_global, spreadsheet_global = exportGlobalVariables()


def run():
    updateGlobalVariables()
    global start_date_global, num_days_global
    try:
        datetime_object = datetime.strptime(start_date_global, '%Y-%m-%d')
    except:
        popup("Error", "Improper Date")
        return
    popup("Running...", "")
    try:
        cycle1 = Cycle(int(num_days_global), datetime_object)
        cycle1.buildCycle()
        cycle1.dispCycle()
        cycle1.outputExcel()
        popup("Success", "Ran Successfully")
    except SameDayMustMustNotError as e:
        popup("Error", e.message)
    except TwoStaffConflict as e:
        popup("Error", e.message)
    except:
        popup_large("Error While Running", traceback.format_exc())

class HomePage:
    def __init__(self, master):
        master.geometry("630x350")
        # Control the Menu Bar
        color1 = "#4d95d4"  # Colour of background
        frame1 = Frame(master, height=450, width=800)
        frame1.pack(side=LEFT, anchor=NW)

        # Info Frame
        info_frame = Frame(frame1, height=450, width=400, bg=color1)
        info_frame.place(x=400, y=0)

        start_date_label = Label(info_frame, text="Start Date: N/A", width=18, height=2, font=('Ariel', 14), bg=color1)
        start_date_label.place(x=10, y=20)

        num_days_label = Label(info_frame, text="Num Days in Cycle: N/A", width=18, height=2, font=('Ariel', 14), bg=color1)
        num_days_label.place(x=10, y=110)

        spreadsheet_label = Label(info_frame, text="SpreadSheet: False", width=18, height=2, font=('Ariel', 14), bg=color1)
        spreadsheet_label.place(x=10, y=200)

        # Main Buttons
        new_cycle_button = Button(frame1, text="1. Create New Cycle", command=lambda: popup_input(), width=18, height=2, font=('Ariel', 14))
        new_cycle_button.place(x=50, y=20)

        refresh_button = Button(frame1, text="2. Refresh", command=lambda: refresh_variables(start_date_label, num_days_label, spreadsheet_label), width=14, height=2,
                                font=('Ariel', 14))
        refresh_button.place(x=50, y=80)

        run_button = Button(frame1, text="3. Run", command=lambda: threading.Thread(target=run).start(), width=14, height=2, font=('Ariel', 14))
        run_button.place(x=50, y=140)

        download_button = Button(frame1, text="4. Download", command=lambda: download_output(), width=14, height=2,
                         font=('Ariel', 14))
        download_button.place(x=50, y=200)

# -----------------------------------------------------------


def main():
    global window
    window = Tk()
    window.wm_title("DayOffScheduler")
    HomePage(window)

    # Set size of the window to not change.
    windowx = 630
    windowy = 350
    window.minsize(windowx, windowy)
    window.maxsize(windowx, windowy)

    window.mainloop()


main()
# Settings page - Trip date difference,
