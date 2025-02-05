import numpy as np
arr=np.array([[1,5,6],
              [4,7,2],
              [3,1,9]])

print('Largest element is:',arr.max())
print('Row-wise maximum elements:',arr.max(axis=1))

print('Coloum-wise minimum elements:',arr.min(axis=0))

print('Sum of all array elements:',arr.sum())
#cumulative
print('cumulative sum along each row:\n',arr.cumsum(axis=1))

print('cumulative sum along each column:\n',arr.cumsum(axis=1))
