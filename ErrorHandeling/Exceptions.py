from GUI.guiHelperFunctions import *

class Error(Exception):
    """Base class for other exceptions"""
    pass


class SameDayMustMustNotError(Error):
    def __init__(self, name, incorrect_date):
        self.name = name
        self.incorrect_date = incorrect_date
        self.message = self.name + " is set to be on day off but is required to be not on day off on " + self.incorrect_date
        super().__init__(self.message)

class TwoStaffConflict(Error):
    def __init__(self, name, name2):
        self.name = name
        self.name2 = name2
        self.message = self.name + " and " + self.name2 + " must be on the same day off but they can't be!"
        super().__init__(self.message)
