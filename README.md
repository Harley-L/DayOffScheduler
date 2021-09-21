# DayOffScheduler
### Welcome to the DOFF Scheduler. This is a guide to help use it and to help understand why it might not be working.

## Installation (from the perspective of the client):
1. Download the exe (approx 175mb)
2. Go through the installation helper and pick a location where to install the application files
3. OPTIONAL: Pin the exe file to your taskbar for easy access



## Usage:
1. Press create new cycle
2. Input the cycle start date in the correct format (YYYY-MM-DD)
3. Input the number of days per cycle (If the start date is July 10th and the number of days is 5, it will go from the 10th-14th)
4. Upload the spreadsheet by pressing the upload spreadsheet button (Make sure the file is named: CampDoffSchedule.xlsx)
5. After entering all information, make sure to press the Okay button, to close the create new cycle window (Sometimes it hides behind windows)
6. Press the refresh button to double-check that all information is entered correctly
7. If not correct, you can just press the create new cycle button again to update the information
8. Press the run button (It might take a while, don't be alarmed if the program says (Not Responding))
9. Once complete it will say Run Successful
10. Click the download button and the output will be in your downloads folder called "output.xlsx"



## Things to know:
**Drama:** 
Drama is a complicated activity. To properly use the day off scheduler for drama, each specialist should be listed as "Drama Sr" or "Drama Jr" depending on if it is currently the Jr or Sr play, instructors should be given the activity tag "Drama Sr" or "Drama Jr". The PD can keep both the "Drama Sr" and "Drama Jr" activities.

**Dates:** 
When inputting data into excel, make sure that EXCEL recognizes it as a proper date. You can just write "Aug 20" and it would automatically recognize it as a proper date.

**Other Cells:** 
Make sure that any field that is not a date is the "General" type. Dates should automatically switch to "Custom" type.

**Trip Dates:** 
Currently, trip dates should be input exactly. The day off scheduler will not allow the counsellor to go on day off the two days prior.
(This can be changed in DataProccessing\importantDates.py in the getTripDates function: `day = sdate + timedelta(days=i-2))` (change the 2)


## Conflicts in output.xlsx:
1. Manually said _____ cannot be on this day off: Could be because Trip, MUST NOT Date, On DOFF 48 Hours before
2. Can't be on the same day off as another staff - self-explanatory

## Common Errors:
**The exe won't open or something along the lines of the program failed:**
*Solution: There was a problem with the installer or one of the files got corrupted. Delete the program files and reinstall using the exe installer. If that doesn't work, try on another computer.*

**Create new cycle Error: Undefined: Start Date/Number of Days/Spreadsheet**
*Solution: You did not input information for the start date or number of days in cycle. Click create new cycle again and enter the information before pressing ok. If it could not find the spreadsheet, manually put the correct spreadsheet in the Spreadsheets folder in the program files. Enter the cycle start date/number of days like normal, ignore the error, and run the program.*

**Refresh Button**
Any problems with the refresh button is not going to be of any consequence. It is just to double-check that all info is correct on the program's side. *Solution: Make sure to input the correct information to avoid errors with the refresh button!*

**Run button errors:**
If any information is entered incorrectly, or information that is entered conflicts with each other, there will be an error. It is very explicit in the error for example it can say that two staff can't be on the same day off. *Solution: In this case just make the changes in the spreadsheet and rerun after inputting the information again.*
Another error is a staff is set to be on a day off but is required not to be on that same day off. *Solution: In this case just make the changes in the spreadsheet and rerun after inputting the information again.*
The run button may stop loading after a while and NO confirmation pop-up window appears. *Solution: Data is improperly given to the program. Go over the spreadsheet and verify everything is proper.*

**Download button errors:**
Download button is not making the output go to your downloads folder *Solution: Don't worry, the program ran fine, just go to the program files and open the output.xlsx file in the Spreadsheets folder.*
