n=int(input("Enter the number"))
for row in range (n):
    for col in range (0,n):
        if row==0 or col==(n-1) or col==row:
            print("*",end="")
        else:
            print(end=" ")
    print()