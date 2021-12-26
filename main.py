class Car:
    isCarRun = False
    @staticmethod
    def run():
        if(Car.isCarRun):
            print('CAR IN RUNING')
        else:
            print('CAR IN NOT RUN')

Car.run()