import numpy as np
# crearing array from list with type float
a= np.array([[1,2,3],[5,6,7]],dtype = 'float')
print('Array created using passed list:\n',a)

# creating array from tuple
b= np.array((1,2,3))
print('\nArray created using passes tuple:\n',b)

#creating a 3x4 array with all zeros
c=np.zeros((3,4))
print('\nAn array initilized with all zeros:\n',c)

#creating a 3x4 array with all ones
d=np.ones((3,4))
print('\nAn array initilized with all zeros:\n',d)

#creating a constant value array of complex type
e=np.full((3,3),6,dtype='complex')
print('\nAn array initilized with all 6s.'
      'Array type is complex:\n',e)

#creating a constant value array of integer type
e=np.full((3,3),6,dtype='int')
print('\nAn array initilized with all 6s.'
      'Array type is int:\n',e)
#creating a constant value array of float type
e=np.full((3,3),6,dtype='float')
print('\nAn array initilized with all 6s.'
      'Array type is float:\n',e)

#create an array with random values
e=np.random.random((2,2))
print('\nA random array:\n',e)

#creating of sequence of integers
#from 0 to 30 with steps of 5
f= np.arange(0,30,5)
print('\nA sequential array with step of 5:\n',f)

g=np.linespace(0,5,4)
print('sequence array with 4 values between''0 and 5:\n',g)



