class Radio:
    brand=None
    wave=None
    source=None
    activeChannel=None
    channels = []
    on=False

    def __init__(self, brand, wave, source):
        self.brand = brand
        self.wave = wave
        self.source = source

    def turnOn(self):
        self.on = True
        self.scanChannel()

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

carRadio = Radio('Simbada', 'FM', 'DC')
carRadio.turnOn()
carRadio.scanChannel()
carRadio.setChannel(carRadio.channels[4])
carRadio.printData()

carRadio.turnOff()
carRadio.printData()

# Home

homeRadio = Radio('SHARP', 'AM/FM', 'AC')

homeRadio.turnOn()
homeRadio.scanChannel()
homeRadio.setChannel(homeRadio.channels[4])
homeRadio.printData()

homeRadio.turnOff()
homeRadio.printData()