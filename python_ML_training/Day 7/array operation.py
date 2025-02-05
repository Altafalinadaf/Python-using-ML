import numpy as np
a= np.array([1,2,5,3])

print('Adding 1 to every element:',a+1)

print('subtracting 3 from each element:',a-3)

print('multiplying each element by 10:',a*10)

print('squaring each element:',a**2)

#modify exesting array
a*=2
print('Doubled each element of original array:',a)

#transpose of array
a=np.array([[1,2,3],[3,4,5],[9,6,0]])

print('\noriginal array:\n',a)
print('Transpose of array:\n',a.T)