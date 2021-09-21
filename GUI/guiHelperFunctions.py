from GUI.guiImports import *

start_date_global = "N/A"
num_days_global = "N/A"
spreadsheet_global = False

def exportGlobalVariables():
    return start_date_global, num_days_global, spreadsheet_global


def get_download_path():
    """Returns the default downloads path for linux or windows"""
    if os.name == 'nt':
        sub_key = r'SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders'
        downloads_guid = '{374DE290-123F-4565-9164-39C4925E467B}'
        with winreg.OpenKey(winreg.HKEY_CURRENT_USER, sub_key) as key:
            location = winreg.QueryValueEx(key, downloads_guid)[0]
        return location
    else:
        return os.path.join(os.path.expanduser('~'), 'downloads')


def download_output():
    try:
        if platform == "darwin":
            downloads_path = str(Path.home() / "Downloads")
            downloads_path = downloads_path + "/output.xlsx"
            output_path = get_mac_directory() + "/Spreadsheets/output.xlsx"
        else:
            downloads_path = get_download_path()
            downloads_path = os.path.join(downloads_path, "output.xlsx")
            output_path = os.getcwd() + "/Spreadsheets/output.xlsx"
        shutil.copyfile(output_path, downloads_path)
        popup("Success", "Downloaded Successfully")
    except:
        popup("Error", "Downloaded Failed")


def refresh_variables(start_date_label, num_days_label, spreadsheet_label):
    start_date_label.config(text=f"Start Date: {start_date_global}")
    num_days_label.config(text=f"Num Days in Cycle: {num_days_global}")
    spreadsheet_label.config(text=f"SpreadSheet: {spreadsheet_global}")

def ChangeScreen(window, screen, frame):
    for widget in frame.winfo_children():
        widget.destroy()
    screen(window)


def popup(title, given_message):  # Popup when an image is successfully uploaded
    # Initialize popup
    win = Toplevel()
    win.wm_title(title)
    winx = 450
    winy = 200
    win.minsize(winx, winy)
    win.maxsize(winx, winy)
    win.geometry("400x300+400+200")

    # Title of the popup
    message = Label(win, text=title, font=('Ariel', 20))
    message.pack(side=TOP, pady=10)

    # Message of the popup
    if len(given_message) > 45:
        given_message1 = given_message[0:45]
        given_message2 = given_message[45:len(given_message)]
        message = Label(win, text=given_message1, font=('Ariel', 13))
        message.pack(side=TOP, pady=6)
        message = Label(win, text=given_message2, font=('Ariel', 13))
        message.pack(side=TOP)
    else:
        message = Label(win, text=given_message, font=('Ariel', 13))
        message.pack(side=TOP, pady=10)

    # Create canvas
    canvas = Canvas(win, width=winx, height=winy)
    canvas.pack(side=LEFT)

    # Exit button to close the popup window
    exitpop = Button(win, text="Okay", command=win.destroy, height=2, width=12)
    exitpop.place(x=(winx/2)-55, y=winy-60)


def popup_large(title, given_message):  # Popup when an image is successfully uploaded
    # Initialize popup
    win = Toplevel()
    win.wm_title(title)

    win.geometry("600x400+400+200")

    Grid.columnconfigure(win, 0, weight=1)

    Grid.rowconfigure(win, 0, weight=1)
    Grid.rowconfigure(win, 1, weight=3)
    Grid.rowconfigure(win, 2, weight=1)

    # Title of the popup
    message = Label(win, text=title, font=('Ariel', 20))
    message.grid(row=0, column=0, sticky="nsew")

    # Message of the popup
    message2 = Label(win, text=given_message, font=('Ariel', 13), borderwidth=0, anchor="w", justify=LEFT)
    message2.grid(row=1, column=0, sticky="new", pady=10, padx=4)

    # Exit button to close the popup window
    exitpop = Button(win, text="Okay", command=win.destroy, height=2, width=12)
    exitpop.grid(row=2, column=0, sticky="s", pady=10)


def popup_input():  # Popup when an image is successfully uploaded
    # Initialize popup
    win = Toplevel()
    win.wm_title("New Cycle")
    winx = 450
    winy = 270
    win.minsize(winx, winy)
    win.maxsize(winx, winy)
    win.geometry("450x270+400+200")

    # Title of the popup
    message = Label(win, text="Create New Cycle", font=('Ariel', 20))
    message.pack(side=TOP, pady=10)

    start_date_label = Label(win, text="Cycle Start Date(YYYY-MM-DD)", font=('Ariel', 12))
    start_date_label.place(x=10, y=58)

    # User Input field
    start_date_input = Entry(win)
    start_date_input.place(x=240, y=60)
    start_date_input.focus_set()

    num_days_label = Label(win, text="Number Days in Cycle", font=('Ariel', 12))
    num_days_label.place(x=10, y=98)

    # User Input field
    num_days_input = Entry(win)
    num_days_input.place(x=240, y=100)
    num_days_input.focus_set()

    upload_excel = Button(win, text="Upload SpreadSheet", command=lambda: openExcelSheet(), height=2,
                     width=18)
    upload_excel.place(x=(winx / 2) - 55, y=winy - 115)

    # Exit button to close the popup window
    exitpop = Button(win, text="Okay", command=lambda: exit_input(win, start_date_input, num_days_input), height=2, width=12)
    exitpop.place(x=(winx/2)-38, y=winy-60)


def exit_input(win, start_date_input, num_days_input):
    global start_date_global, spreadsheet_global, num_days_global
    start_date, num_days = captureUserInput(start_date_input, num_days_input)
    error = 0
    error_message = 'Undefined: '
    if start_date == '':
        error += 1
        error_message += "Start Date"
    if num_days == '':
        if error > 0:
            error_message += "/"
        error += 1
        error_message += "Number of Days"
    if os.name == 'nt':
        dir_spreadsheets = os.getcwd() + '/Spreadsheets'
    else:
        dir_spreadsheets = get_mac_directory() + "/Spreadsheets"
    numSpreadSheets = len([name for name in os.listdir(dir_spreadsheets) if os.path.isfile(os.path.join(dir_spreadsheets, name))])
    if numSpreadSheets <= 0:
        if error > 0:
            error_message += "/"
        error += 1
        error_message += "Spreadsheet"
    else:
        spreadsheet_global = True
    if error > 0:
        popup("Error", error_message)
    start_date_global = start_date
    num_days_global = num_days
    win.destroy()


def openExcelSheet():
    # Open the excel sheet
    file1 = fd.askopenfile(mode="r")
    fileaddress = file1.name

    # Get the excel spreadsheet name
    filename = ''
    for letter in fileaddress:
        filename += letter
        if letter == '/':
            filename = ''

    # Copy spreadsheet to folder
    if os.name == 'nt':
        excelfolder_dir = os.getcwd() + "/Spreadsheets"  # Find images folder
    else:
        excelfolder_dir = get_mac_directory() + "/Spreadsheets"  # Find images folder

    shutil.copyfile(file1.name, os.path.join(excelfolder_dir, filename))


# Capture user input
def captureUserInput(start_date_input, num_days_input):
    start_date = start_date_input.get()
    num_days_input = num_days_input.get()
    return start_date, num_days_input
