class Car1:
    a = "This is Car1 Calss"

    @staticmethod
    def start():
        print("Car1 class Method start")

class Car2(Car1):
    b = "This is Car2 Calss"
    @staticmethod
    def end():
        print("Car2 class Method end")

class Car3(Car2):
    c = "This is Car3 Class"

c3 = Car3()
print(c3.c)
print(c3.b)
print(c3.a)
c3.start()
c3.end()