from abc import ABC, abstractmethod

# Abstract Class
class Animal():
    @abstractmethod
    def sound(self):
        pass   # no body (just an abstract method)

# Concrete Class
class Dog(Animal):
    def sound(self):
        print("Dog says: Woof Woof!")

# Concrete Class
class Cat(Animal):
    def sound(self):
        print("Cat says: Meow Meow!")

# Create objects
d = Dog()
d.sound()  # Output: Dog says: Woof Woof!

c = Cat()
c.sound()  # Output: Cat says: Meow Meow!

