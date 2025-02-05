print('welcome to mk shopping cart')
total=0
def category():
    ch=int(input('choose the category\n 1.electronic 2.furniture 3.applinces 4.cloths 5.bill\n'))
    if ch==1:
        electronic()
    elif ch==2:
        furniture()
    elif ch==3:
        applinces()
    elif ch==4:
        cloths()
    elif ch==5:
        bill()
def electronic():
    global total
    ch2=int(input('enter what you want\n 1.mobile=10000 2.earbuds=599 3.speakers=799 4.cables=99 5.skip\n'))
    if ch2==1:
        total= total+10000
    elif ch2==2:
        total=total+599
    elif ch2==3:
        total=total+799
    elif ch2==4:
        total=total+99
    elif ch2==5:
        category()
def furniture():
    global total
    ch3=int(input('enter what you want\n 1.sofaset=30000 2.bed=5959 3.chairs=499 4.dining table=9999 5.skip\n'))
    if ch3==1:
        total= total+30000
    elif ch3==2:
        total=total+5959
    elif ch3==3:
        total=total+499
    elif ch3==4:
        total=total+9999
    elif ch3==5:
        category()
def applinces():
    global total
    ch4=int(input('enter what you want\n 1.mixer=599 2.cooker=699 3.fridge=7999 4.micro ovean=999 5.skip\n'))
    if ch4==1:
        total= total+599
    elif ch4==2:
        total=total+699
    elif ch4==3:
        total=total+7999
    elif ch4==4:
        total=total+999
    elif ch4==5:
        category()
def cloths():
    global total
    ch4=int(input('enter what you want\n 1.shirts=399 2.pants=699 3.jackets=999 4.kurta=999 5.skip\n'))
    if ch4==1:
        total= total+399
    elif ch4==2:
        total=total+699
    elif ch4==3:
        total=total+999
    elif ch4==4:
        total=total+999
    elif ch4==5:
        category()
def bill():
    global total
    print('price= ',total)
    gst=0.18*total
    tc = 100
    if(total==0):
        print( 'total=0\n not purchased yet')

    elif (total<500):


        gt = total + gst+tc
        print('gst is',gst)
        print('tc is',tc)
        print('the  total is:',gt)



    else:
        gt=total+gst
        print('gst is',gst)
        print('your total= ',gt)




    if gt>1500:

        cou = input("do you have coupon y or n")
        if cou == 'y':
            dis=total*0.30
            total=gt-dis


            token = input("enter the code ")
            if token == '12345':
                    print('token is valid')
                    print('discount is',dis)
                    print('total is',total)
                    print('thankyou for shopping')

            else:
                print(' invalid')



while True:
    category()





