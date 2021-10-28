class Radio:
    __channels = []
    __activeChannel = None

    def __init__(self):
        self.__scan()

    def __scan(self):
        print('scan channel')
        self.__channels = [1, 2, 3]

    def _setChannel(self):
        print('set channel')
        self.__activeChannel = self.__channels[0]

    def getActiveChannel(self):
        return self.__activeChannel


# Car
class FMRadio(Radio):
    def __init__(self):
        super(FMRadio, self).__init__()
        self._setChannel()



carRadio = FMRadio()
print(carRadio.getActiveChannel())
