# import RPi.GPIO as IO
# import time
import sys
import getopt
from alarm import setUpAlarm


ioPorts = [3, 5, 7, 8, 10, 11, 12, 13, 15, 16, 18, 19, 21, 22, 23, 24, 26, 29, 31, 32, 33, 35, 36, 37, 38, 40]
groundPorts = [6, 9, 14, 20, 25, 30, 34, 39]
uselessPorts = [1, 2, 4, 17, 27, 28]
inUsePorts = []

allPorts = set(ioPorts)
allPorts.update(groundPorts)
allPorts.update(uselessPorts)


def check():
    if len(allPorts) != 40:
        print("ААААААААААА ПЛАТА ГОРИТ ТУШИ (Count)\n")
        exit(1)
    if len(ioPorts) != 26 or len(groundPorts) != 8 or len(uselessPorts) != 6:
        print("ААААААААААА ПЛАТА ГОРИТ ТУШИ (IO)\n")
        exit(1)


class IoPort(object):
    def __init__(self, numPort):
        if (numPort not in ioPorts) or (numPort in inUsePorts):
            print("ПОРТ НЕПРАВИЛЬНО УКАЗАН ВСЁ СГОРИТ (Init)\n")
            exit(2)
        self.__ioPort = numPort
        self.__voltage = 0
        inUsePorts.append(numPort)
        # IO.setup(self.__ioPort, IO.OUT)
        # IO.output(self.__ioPort, self.__voltage)

    def get(self):
        if not (self.__ioPort in inUsePorts):
            print("ПОРТ НЕПРАВИЛЬНО УКАЗАН ВСЁ СГОРИТ (Get)\n")
            exit(2)
        return self.__ioPort

    def lightOn(self):
        if self.__voltage == 1:
            print('Два раза зажгли одно и то же!!!\n')
            exit(3)
        self.__voltage = 1
        print('Порт номер ', self.__ioPort, ' светится\n')
        # IO.output(self.__ioPort, self.__voltage)

    def lightOff(self):
        if self.__voltage == 0:
            print('Два раза выключили одно и то же!!!\n')
            exit(3)
        self.__voltage = 0
        print('Порт номер ', self.__ioPort, ' мрак\n')
        # IO.output(self.__ioPort, 0)

    def isLightOn(self):
        return self.__voltage == 1


def outForDebug(boolean):
    if boolean:
        print(1, end=' ')
    else:
        print(0, end=' ')


def debugShow(debugPorts):
    if len(debugPorts) != 12:
        print('Чето тут не так переделывай')
        exit(4)
    for i in range(0, 7):
        for j in range(0, 7):
            if i == 0 and j == 3:
                outForDebug(debugPorts[0].isLightOn())
            elif i == 1 and j == 4:
                outForDebug(debugPorts[1].isLightOn())
            elif i == 2 and j == 5:
                outForDebug(debugPorts[2].isLightOn())
            elif i == 3 and j == 6:
                outForDebug(debugPorts[3].isLightOn())
            elif i == 4 and j == 5:
                outForDebug(debugPorts[4].isLightOn())
            elif i == 5 and j == 4:
                outForDebug(debugPorts[5].isLightOn())
            elif i == 6 and j == 3:
                outForDebug(debugPorts[6].isLightOn())
            elif i == 5 and j == 2:
                outForDebug(debugPorts[7].isLightOn())
            elif i == 4 and j == 1:
                outForDebug(debugPorts[8].isLightOn())
            elif i == 3 and j == 0:
                outForDebug(debugPorts[9].isLightOn())
            elif i == 2 and j == 1:
                outForDebug(debugPorts[10].isLightOn())
            elif i == 1 and j == 2:
                outForDebug(debugPorts[11].isLightOn())
            else:
                print(' ', end=' ')
        print()


def main():
    check()
    # IO.setmode(IO.BOARD)
    ports = []

    for i in range(0, 12):
        ports.append(IoPort(ioPorts[i]))
    if len(ports) != 12:
        print("ПОРТОВ МНОГО ИЛИ МАЛО РАЗБЕРИСЬ\n (12)")
        exit(3)

    debugShow(ports)
    try:
        opts, args = getopt.getopt(sys.argv[1:], "t", ["time="])
    except:
        print("Неправильно параметры передал, лох!")
        sys.exit(2)

    for opt, arg in opts:
        if opt in ("-t", "--time"):
            setUpAlarm(ports, arg)
    return 0


if __name__ == '__main__':
    main()
