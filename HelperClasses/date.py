from HelperClasses.classImports import *

def convertToDate(date):
    date2 = ""
    for char in date:
        if char == ' ':
            break
        date2 = date2 + char

    return Date(date2[8:10], date2[6:7], date2[0:4])

class Date:
    def __init__(self, *args):
        if len(args) > 1:
            try:
                if args[0] > 31 or args[0] < 1 or args[1] < 1 or args[1] > 12 or args[2] < 0:
                    raise Exception(f"Improper Date {args[0]}/{args[1]}/{args[2]}")
            except:
                pass
            self.day = int(args[0])
            self.month = int(args[1])
            self.year = int(args[2])
        elif len(args) == 1:  # isinstance(args, datetime.datetime):
            self.day = args[0].day
            self.month = args[0].month
            self.year = args[0].year
        else:
            raise Exception("Improper Date")

    def isDateWithin(self, bottom, top):
        if not (self.year >= bottom.year and self.year <= top.year):
            return False
        if not (self.month >= bottom.month and self.month <= top.month):
            return False
        if not (self.day >= bottom.day and self.day <= top.day):
            return False
        return True

    def isDateIn(self, arrayOfDates):
        for i in range(len(arrayOfDates)):
            if self.toString() == arrayOfDates[i].toString():
                return True
        return False

    def toString(self):
        if self.month < 10 and self.day < 10:
            return str(self.year) + "-0" + str(self.month) + "-0" + str(self.day)
        if self.month < 10:
            return str(self.year) + "-0" + str(self.month) + "-" + str(self.day)
        if self.day < 10:
            return str(self.year) + "-" + str(self.month) + "-0" + str(self.day)

        return str(self.year) + "-" + str(self.month) + "-" + str(self.day)
