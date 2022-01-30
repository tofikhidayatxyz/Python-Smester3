import hashlib
from xmlrpc.client import boolean

# class Tv:
#     channels =  ['Rcti', 'TVri', 'MNC', 'NET.']
#     channes = None
#     brand = None
#     resolution = None
#     isOn = False

#     def __init__(self, brand, size):
#         self.brand = brand
#         self.size = size

#     def setChannel(self, index):
#         if(self.isOn) :
#             self.channel = self.channels[index]
#         else :
#             print('Tv should be on !')

#     def addChannel(self, newChannel) :
#         if(self.isOn) :
#             self.channels.append(newChannel)
#         else :
#             print('Tv should be on !')
    
#     def manualRemove(self, toDelete):
#         if(self.isOn) :
#             try:
#                 self.channels.remove(toDelete)
#             except Exception as ex :
#                 print(ex)
#         else :
#             print('Tv should be on !')
       
    
#     def turnOn(self):
#         self.isOn = True

#     def turnOff(self):
#         self.isOn = False

#     def removeChannel(self, toDelete):
#         self.channels = list(filter(lambda x : x != toDelete, self.channels))

#     # Hiraukan di bawah ini
#     @classmethod
#     def tvSharp(cls, size):
#         print('Class method initialized')
#         return cls('Sharp',  size)
#     # Destruct
#     def __del__(self):
#         print(F'This {self.brand}  object has been deleted')

# # Static method
#     @staticmethod
#     def createTv():
#         return Tv('LG', '21 inch')


# # prints
# tvRuangTamu = Tv.createTv()
# print(tvRuangTamu.channels)
# tvRuangTamu.setChannel(1)
# tvRuangTamu.turnOn()
# tvRuangTamu.addChannel('ANTV')
# print(tvRuangTamu.channels)
# tvRuangTamu.removeChannel('TVri')
# print(tvRuangTamu.channels)
# tvRuangTamu.removeChannel(1)
# print(tvRuangTamu.channels)
# tvRuangTamu.manualRemove('MNCS')
# tvRuangTamu.turnOff()
# print(tvRuangTamu.__dict__)



class User:
    __password = None
    def __init__(self) -> None:
        pass

    def _setPassword(self, newPassword):
        self.__password = hashlib.sha256(str(newPassword).encode('utf-8')).hexdigest()

    def _comparePassword(self, toCompare) -> boolean:
        return self.__password == hashlib.sha256(str(toCompare).encode('utf-8')).hexdigest()
    


class Student(User):
    def __init__(self) -> None:
        super(Student).__init__()



user1 = Student()



user1._setPassword("assw")
print(user1._comparePassword("assw"))



print(user1.__dict__)