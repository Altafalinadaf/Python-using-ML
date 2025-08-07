class Car:
    name = "abs"
    print("this is the Car Class")
    def __init__(self):
        
        print("this is python constructor")
    
    def Car(name):
        print("this function belongs to Car class",name)

#this one calling Car cls which create obj of Car cls then Constructor will get invoke
# it wil print  "this is python constructor"
Car() 

# this will calls Car function inside Car Class 
# this wil print "this function belongs to Car class"
Car.Car("abc")

# creting Car()
#  this one print "this is method"

def Car():
    print("this is method")

Car()