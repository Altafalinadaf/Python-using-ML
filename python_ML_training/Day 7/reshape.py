import numpy as np
arr=np.array([[1,2,3,4],
              [5,6,7,4],
              [1,2,0,4]])
newarr1= arr. reshape(2,2,3)
newarr2= arr.reshape(4,3)

print('\noriginal array\n',arr)
print('reshaped array:\n',newarr1)
print('reshaped array2:\n',newarr2)



