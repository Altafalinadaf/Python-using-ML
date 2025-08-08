class A:
    def method1(self):
        print("class is A")

class B:
    def method2(self):
        print("class is B")

class C(A,B):
    def method3(self):
        print("class is C")

c = C()
c.method3()
c.method2()
c.method1()