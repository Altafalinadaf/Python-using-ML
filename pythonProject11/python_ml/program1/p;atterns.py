for row in range(5):
    for col in range(5):
        if col==0 or row==4 or col==row:
            print("*",end="")
        else:
            print(end=" ")
    print()