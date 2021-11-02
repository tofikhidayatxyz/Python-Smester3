class Radio:
    brand=None
    wave=None
    source=None
    activeChannel=None
    channels = []
    on=False

    def __init__(self, brand, source):
        self.brand = brand
        self.source = source

    def __getActiveIndex(self):
        currentActive = -1
        try:
            currentActive  = self.channels.index(self.activeChannel)
        except:
            currentActive = -1
        return  currentActive

    def turnOn(self):
        self.on = True
        self.scanChannel()
        self.activeChannel = None

    def turnOff(self):
        self.on = False
        self.channels = []
        self.activeChannel = None

    def scanChannel(self):
        newChannels = []
        for i in range(87, 108):
            newChannels.append(i)
        self.channels = newChannels

    def setChannel(self, newChannel):
        self.activeChannel = newChannel

    def setChannelUp(self):
        if self.__getActiveIndex() == len(self.channels) - 1:
            self.activeChannel = 0
        else:
            self.activeChannel = self.__getActiveIndex() + 1

    def setChannelDown(self):
        if self.__getActiveIndex() == 0:
            self.activeChannel = len(self.channels) - 1
        else:
            self.activeChannel = self.__getActiveIndex() - 1

    def _cleanChannel(self):
        self.activeChannel = None
        self.channels = []

    def __add__(self, other):
        return len(self.channels) + len(other.channels)

    def printData(self):
        print("------------------------------")
        print(f'Brand : {self.brand}')
        print(f'Wave : {self.wave}')
        print(f'On  : {"Nyala" if self.on else "Mati" }')
        print(f'Source : {self.source}')
        print(f'Channels : {self.channels}')
        print(f'Active Channel : {self.activeChannel}')
        print("------------------------------\n")

# Car
class AMRadio(Radio):
    def __init__(self, brand, source):
        super(AMRadio, self).__init__(brand, source)
        self.wave = 'AM'
        self._cleanChannel()

    def scanChannel(self):
        newChannels = []
        for i in range(530, 1700):
            newChannels.append(i)
        self.channels = newChannels


class FMRadio(Radio):
    def __init__(self, brand, source):
        super(FMRadio, self).__init__(brand, source)
        self.wave = 'FM'
        self._cleanChannel()

    def scanChannel(self):
        newChannels = []
        for i in range(87, 108):
            newChannels.append(i)
        self.channels = newChannels




carRadio = FMRadio('Simbada', 'DC')
carRadio.turnOn()
carRadio.scanChannel()
carRadio.setChannelUp()
carRadio.setChannel(carRadio.channels[4])
carRadio.printData()
#
# carRadio.turnOff()
# carRadio.printData()

# Home

homeRadio = AMRadio('SHARP', 'AC')
homeRadio.turnOn()
homeRadio.scanChannel()
homeRadio.setChannel(homeRadio.channels[4])
carRadio.setChannelDown()
homeRadio.printData()

# homeRadio.turnOff()
# homeRadio.printData()
 # magic method

print(f"Total ada {carRadio + homeRadio} Channels")
