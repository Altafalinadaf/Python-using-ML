while True:
    a = int(input('enter the salary'))
    da = 0.4 * a
    hra = 0.2 * a
    bs = a - da - hra
    ch=int(input("what do you wanne know ? \n 1.hra 2.da 3.bs 4.details" ))
    if ch==1:
       print('hra is',hra)
    elif ch==2:
       print('da is',da)
    elif ch==3:
        print('bs is',bs)
    elif ch==4:
        print('hra is',hra)
        print('da is', da)
        print('bs is', bs)
    else:
         print("invalid")


