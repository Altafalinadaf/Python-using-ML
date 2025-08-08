class Car1:
    varA="This is Car1 Class"

class Car2(Car1):
    varB="This is Car2 Class"

c = Car2()
print(c.varB)
print(c.varA,end="")