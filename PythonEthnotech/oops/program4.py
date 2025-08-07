class Student:
    def __init__(self, fullname):
        self.name = fullname   # Save the name in the object
        print(fullname)

    def hello(self,marks):          # 'self' refers to the same student
        print("hello",self.name,"you marks are :",marks)

s1 = Student("karan")
s1.hello(65)   # prints: hello karan