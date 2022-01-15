
import sys


class Car:
    isCarRun = False
    @staticmethod
    def run():
        if(Car.isCarRun):
            print('CAR IN RUNING')
        else:
            print('CAR IN NOT RUN')

class Lamborgini(Car):
    def __init__(self):
        super(Lamborgini).__init__()
    @staticmethod
    def gas():
        try :
            Lamborgini.runAll()
        except:
            print('OOPSSSSSSSS ERROR \n ', sys.exc_info)

Lamborgini.gas()