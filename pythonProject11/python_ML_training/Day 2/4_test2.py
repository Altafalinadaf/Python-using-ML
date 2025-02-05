while True:
    a=int(input('enter the salary'))
    if(a<50000):
        print('nill')
    elif a>50000 and a<60000:
        b=a-50000
        t=b*0.1
        print('taxable amount to b paid is',t)
    elif a>60000 and a<150000:
        b=a-50000
        t=b*0.2
        print('taxable amount to b paid is',t)
    else:
        a>150000
        b=a-50000
        t=b*0.3
        print('taxable amount to b paid is',t)