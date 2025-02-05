def add():
    a=int(input('enter the number'))
    b=int(input('enter the number'))
    sum=(a+b)
    print(sum)
def sub():
    a = int(input('enter the number'))
    b = int(input('enter the number'))
    sub=(a - b)
    print(sub)
def div():
    a=int(input('enter the number'))
    b=int(input('enter the number'))
    div=(a/b)
    print(div)
def mul():
    a = int(input('enter the number'))
    b = int(input('enter the number'))
    mul=(a * b)
    print(mul)

while True:
    ch=int(input("enter the choice\n 1.add 2.sub 3.div 4.mul"))
    if ch==1:
        add()
    elif ch==2:
        sub()
    elif ch==3:
        div()
    elif ch==4:
        mul()
    else:
         print('sum is invalid')
