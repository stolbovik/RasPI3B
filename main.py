# import RPi.GPIO as IO
# import time

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
        inUsePorts.append(numPort)
        # IO.setup(self.__ioPort, IO.OUT)
        # IO.output(self.__ioPort, 0)

    def get(self):
        if not (self.__ioPort in inUsePorts):
            print("ПОРТ НЕПРАВИЛЬНО УКАЗАН ВСЁ СГОРИТ (Get)\n")
            exit(2)
        return self.__ioPort

    def lightOn(self):
        print('Порт номер ', self.__ioPort, ' светится\n')
        # IO.output(self.__ioPort, 1)

    def lightOff(self):
        print('Порт номер ', self.__ioPort, ' мрак\n')
        # IO.output(self.__ioPort, 0)


def main():
    check()
    # IO.setmode(IO.BOARD)
    hoursPorts = []
    minutesPorts = []

    for i in range(0, 12):
        hoursPorts.append(IoPort(ioPorts[i]))
    for i in range(12, 24):
        minutesPorts.append(IoPort(ioPorts[i]))

    if len(hoursPorts) != 12 and len(minutesPorts) != 12:
        print("ПОРТОВ МНОГО ИЛИ МАЛО РАЗБЕРИСЬ\n (12)")
        exit(3)

    return 0


if __name__ == '__main__':
    main()
