print('welcome to xyz ATM')
def cardholder():
    ch = int(input("choose card holder\n "
                   "1.cardholder1 2.cardholder2 3.cardholder3 4.cardholder4"))
    if ch==1:
        cardholder1()
    elif ch==2:
        cardholder2()
    elif ch==3:
        cardholder3()
    elif ch==4:
        cardholder4()
    else:
        print("wrong cardholder")
def cardholder1():
    number=123412341234
    num = int(input("Enter the account number\n"))
    if (num == number):

        print("name=Ali")
        print("number=7337852362")
        print("bank=canara bank")
        print("address=xyz")
        print("Welcome to Canara Bank\n\nInsert your card")

        password = 1234
        balance = 10000
        choice = 0

        pin = int(input("Enter your four digit pin"))

        if (pin == password):
            while choice != 4:
                print("**Menu**")
                print("1.balance")
                print("2.deposit")
                print("3.withdraw")
                print("4.mini statement")
                print("5.cancle")

                choice = int(input("\nEnter you option:\n"))

                if choice == 1:
                    print("Balance =R", balance)
                elif choice == 2:
                    dep = int(input("Enter your doposit:R"))
                    balance += dep
                    print("\n deposite amount:,R", dep)
                    print("balance=R", balance)
                elif choice == 3:
                    num=int(input('enter the number'))
                    if(num==password):
                       wit = int(input("Enter your withdraw amount:R"))
                       balance -= wit
                       print("\nwithdraw amount :,R", wit)
                       print("balance=R", balance)
                elif choice == 4:

                    print("acount holder name=Ali")
                    print("mobile number=7337852362")
                    print("address=xyz")
                    print("Avl balance is", balance)

                elif choice == 5:
                    cardholder()
                else:

                    print("\nInvalid Entry")
        else:
            print("invalid pin")
    else:
        print("invalid number")
def cardholder2():
    number=123412341235
    num = int(input("Enter the account number\n"))
    if (num == number):

        print("name=Khaleel")
        print("number=7337852362")
        print("bank=Panjab bank")
        print("address=xyz")
        print("Welcome to Panjab Bank\n\nInsert your card")

        password = 1235
        balance = 20000
        choice = 0

        pin = int(input("Enter your four digit pin"))

        if (pin == password):
            while choice != 4:
                print("**Menu**")
                print("1.balance")
                print("2.deposit")
                print("3.withdraw")
                print("4.mini statement")
                print("5.cancle")

                choice = int(input("\nEnter you option:\n"))

                if choice == 1:
                    print("Balance =R", balance)
                elif choice == 2:
                    dep = int(input("Enter your doposit:R"))
                    balance += dep
                    print("\n deposite amount:,R", dep)
                    print("balance=R", balance)
                elif choice == 3:
                    num = int(input('enter the number'))
                    if (num == password):
                        num = int(input('enter the number'))
                        if (num == password):

                          wit = int(input("Enter your withdraw amount:R"))
                          balance -= wit
                          print("\nwithdraw amount :,R", wit)
                          print("balance=R", balance)
                elif choice == 4:

                    print("acount holder name=Khaleel")
                    print("mobile number=7337852362")
                    print("address=xyz")
                    print("Avl balance is", balance)

                elif choice== 5:
                    cardholder()
                else:

                    print("\nInvalid Entry")
        else:
            print("invalid pin")
    else:
        print("invalid number")
def cardholder3():
    number=123412341236
    num = int(input("Enter the account number\n"))
    if (num == number):

        print("name=Sanju")
        print("number=7337852362")
        print("bank=Karnataka bank")
        print("address=xyz")
        print("Welcome to Karnataka Bank\n\nInsert your card")

        password = 1236
        balance = 30000
        choice = 0

        pin = int(input("Enter your four digit pin"))

        if (pin == password):
            while choice != 4:
                print("**Menu**")
                print("1.balance")
                print("2.deposit")
                print("3.withdraw")
                print("4.mini statement")
                print("5.cancle")

                choice = int(input("\nEnter you option:\n"))

                if choice == 1:
                    print("Balance =R", balance)
                elif choice == 2:
                    dep = int(input("Enter your doposit:R"))
                    balance += dep
                    print("\n deposite amount:,R", dep)
                    print("balance=R", balance)
                elif choice == 3:
                    num = int(input('enter the number'))
                    if (num == password):

                      wit = int(input("Enter your withdraw amount:R"))
                      balance -= wit
                      print("\nwithdraw amount :,R", wit)
                      print("balance=R", balance)
                elif choice == 4:

                    print("acount holder name=Sanju")
                    print("mobile number=7337852362")
                    print("address=xyz")
                    print("Avl balance is", balance)

                elif choice== 5:
                    cardholder()
                else:

                    print("\nInvalid Entry")
        else:
            print("invalid pin")
    else:
        print("invalid number")
def cardholder4():
    number=123412341237
    num = int(input("Enter the account number\n"))
    if (num == number):

        print("name=Viresh")
        print("number=7337852362")
        print("bank=SBI bank")
        print("address=xyz")
        print("Welcome to SBI Bank\n\nInsert your card")

        password = 1237
        balance = 40000
        choice = 0

        pin = int(input("Enter your four digit pin"))

        if (pin == password):
            while choice != 4:
                print("**Menu**")
                print("1.balance")
                print("2.deposit")
                print("3.withdraw")
                print("4.mini statement")
                print("5.cancle")

                choice = int(input("\nEnter you option:\n"))

                if choice == 1:
                    print("Balance =R", balance)
                elif choice == 2:
                    dep = int(input("Enter your doposit:R"))
                    balance += dep
                    print("\n deposite amount:,R", dep)
                    print("balance=R", balance)
                elif choice == 3:
                    num = int(input('enter the number'))
                    if (num == password):

                       wit = int(input("Enter your withdraw amount:R"))
                       balance -= wit
                       print("\nwithdraw amount :,R", wit)
                       print("balance=R", balance)
                elif choice == 4:

                    print("acount holder name=Viresh")
                    print("mobile number=7337852362")
                    print("address=xyz")
                    print("Avl balance is", balance)

                elif choice == 5:
                    cardholder()
                else:

                    print("\nInvalid Entry")
        else:
            print("invalid pin")
    else:
        print("invalid number")


while True:
    cardholder()

