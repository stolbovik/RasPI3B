import datetime


class Clock:

    def __init__(self):
        self.timeNow = datetime.datetime.now()

    def printTime(self):
        print(str(self.timeNow))
