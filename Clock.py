import datetime
import math
import time

from main import debugShow


class Clock:

    def __init__(self, io_ports_for_clock):
        self.__hourNow = datetime.datetime.now().time().hour
        self.__minuteNow = datetime.datetime.now().time().minute
        self.__secondNow = datetime.datetime.now().time().second
        if self.__hourNow >= 12:
            self.__hourNow -= 12
        self.__IoPorts = io_ports_for_clock
        self.startClock()

    def startClock(self):
        while 1:
            tempMinute = self.__IoPorts[math.floor(self.__minuteNow / 5)].get()
            if not self.__IoPorts[math.floor(self.__minuteNow / 5)].isLightOn():
                print('set minute')
                self.__IoPorts[math.floor(self.__minuteNow / 5)].lightOn()
            if math.floor(self.__minuteNow / 5) != math.floor(self.__secondNow / 5):
                self.__IoPorts[math.floor(self.__secondNow / 5)].lightOn()
            debugShow(self.__IoPorts)
            time.sleep(0.5)
            if math.floor(self.__minuteNow / 5) != math.floor(self.__secondNow / 5):
                self.__IoPorts[math.floor(self.__secondNow / 5)].lightOff()
            debugShow(self.__IoPorts)
            time.sleep(0.5)
            self.__minuteNow = datetime.datetime.now().time().minute
            self.__secondNow = datetime.datetime.now().time().second
            if self.__IoPorts[math.floor(self.__minuteNow / 5)].get() != tempMinute:
                self.__IoPorts[math.floor(self.__minuteNow / 5)].lightOff()