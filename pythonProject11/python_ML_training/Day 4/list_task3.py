l1=[]
ch=int(input('how many element do you wanna enter'))

for i in range(1,ch+1):
    a=int(input('enter the element'))
    l1.append(a)

l1.sort()
print('largest number is', l1[-1])
print('smallest number is', l1[0])

d=len(l1)
a=0
for i in l1:
    a=a+i
    m=a/d
print('mean of l1 is',m)