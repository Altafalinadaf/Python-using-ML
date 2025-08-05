class Student :
    name = "Anil"  # class attribute
    def __init__(self,name):
        self.name=name #object attribute (obj attr has more precidence  than cls attr)
        print(self)
        
# in constructor we always need to pass one arguments which is 'self'
# we can rename to this self, there is no issue with rename
#  The self parameter is a reference of the current instance of the class,
# and is used to access variables that belongs to the class
s2 = Student("mohan") # both are having different obj address
print(s2.name)  
print(s2) # this one and self address will be same

s3= Student("kiran")
print(s3.name)
print(s3) # this one and self address will be same 