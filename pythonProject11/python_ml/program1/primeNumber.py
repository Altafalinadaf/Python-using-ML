def check_prime_number(num):
    if(num==0 | num==1):
        return "not a prime number"
    else :
        for i in range(2,num):
            if(num%i==0):
                return "not a prime number"
    
    return "prime number"
    

def check_prime_number2(num):
    count=0
    if(num==0):
        return "please enter number greather than 0"
    
    for i in range(1,num+1):
        if(num%i==0):
            count+=1
    

    if(count==2):
        return "prime number"
    else:
        return "not prime number"
        




num=int(input("enter the number : "))
print(check_prime_number(num))
print(check_prime_number2(num))

