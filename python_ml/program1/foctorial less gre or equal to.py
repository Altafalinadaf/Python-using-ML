n=int(input("Enter the number:"))
result=1
for i in range(n,0,-1):
    result=result*i
print("factorial of",n,"is",result)