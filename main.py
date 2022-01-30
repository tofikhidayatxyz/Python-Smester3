# Nama: Tofik Hidayat
# NIM: 20200040056
# Kelas: TI 20C

class Tv:
    channels =  ['MNC', 'NET', 'TVRI', 'RAC']
    channel = None
    brand = None
    resolution = None
    isOn = False

    def __init__(self, brand, size):
        self.brand = brand
        self.size = size

    def setChannel(self, index):
        print('Set Channel TV')
        if(self.isOn) :
            self.channel = self.channels[index]
        else :
            print('Tv should be on !')

    def addChannel(self, newChannel) :
        if(self.isOn) :
            self.channels.append(newChannel)
        else :
            print('Tv should be on !')
    
    def manualRemove(self, toDelete):
        print('Remove Channel TV')
        if(self.isOn) :
            try:
                self.channels.remove(toDelete)
            except Exception as ex :
                print(ex)
        else :
            print('Tv should be on !')
    
    def turnOn(self):
        print('Turn On TV')
        self.isOn = True

    def turnOff(self):
        print('Turn Off TV')
        self.isOn = False

    def removeChannel(self, toDelete):
        print('Remove Channel TV')
        self.channels = list(filter(lambda x : x != toDelete, self.channels))


tvs = []


tvs.append(Tv('Sharp', '12'))

def addnewTv():
    brand = input('Isi Brand : ')
    size = input('Isi Ukuran (Inch) : ')

    tvs.append(Tv(brand, size))

def viewTv():
    for index, item in enumerate(tvs):
        print('--------' , (index + 1) , '-----------')
        print('Brand ', item.brand)
        print('Ukuran ', item.resolution)
        print('TV sedang ' , "Menyala" if item.isOn else "Mati")
        print('Channel TV : ' , item.channels)
        print('Channel Aktif : ' , item.channel)
        print("------------------------")

def selectTv():
    print('----------------------')
    index = int(input('Pilih Nomor Tv :'))
    try :
        tv = tvs[index - 1]
        while(True):
            print('----------------------')
            print('Pilih Menu Dari TV ', tv.brand , ': ')
            print('a. Nyalakan')
            print('b. Matikan TV')
            print('c. Ganti Channel')
            print('d. Hapus Channel')
            print('[na]. Back')

            subMenu = input('Pilih Menu : ')

            try:
                if(subMenu == 'a'):
                    tv.turnOn()
                elif(subMenu == 'b'):
                    tv.turnOff()
                elif(subMenu == 'c'):
                    print('Available channels : ', tv.channels)
                    channelIdx = int(input('Masukan Nomor Channel : '))
                    tv.setChannel(channelIdx - 1)
                elif(subMenu == 'd'):
                    print('Available channels : ', tv.channels)
                    channelIdx = int(input('Masukan Index Channel : '))
                    del tv.channels[channelIdx]
                else:
                    break  
            except Exception as e:
                print(e) 
    except Exception as e:
        print(e)
        print('Tv not found')

def removeTv():
    print('--------- HAPUS -----------')
    try :
        tvIdx = int(input('Masukan Index TV : '))
        del tvs[tvIdx - 1]
        print("TV Terhapus")
    except Exception as e:
        print(e)



while(True):
    print('Pilih Menu : ')
    print('1. Tambah TV')
    print('2. Lihat Daftar TV')
    print('3. Pilih TV')
    print('4. Hapus TV')
    print('[na]. End')

    menu = input('Pilih Menu : ')

    if(menu == '1'):
        addnewTv()
        print('----------------------')
    elif(menu == '2'):
        viewTv()
        print('----------------------')
    elif(menu == '3'):
        selectTv()
        print('----------------------')
    elif(menu == '4'):
        removeTv()
        print('----------------------')
    else:
        print('-------- END --------')
        break

