class Car:
    def __init__(self,type):
        self.type= type

    @staticmethod
    def start():
        print("Car Started")

    @staticmethod
    def end():
        print("Car Stopped")

class ToyotaCar(Car):
    def __init__(self,name,type):
        super().__init__(type)
        self.name=name
        print("hello")
        super().start()

car1 = ToyotaCar('prius','electric')
print(car1.type)