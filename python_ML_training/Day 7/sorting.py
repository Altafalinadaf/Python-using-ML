import numpy as np
a = np.array([[1,2,3],
              [3,4,6],
              [0,-1,5]])

#sorting array
print('Array element in sorted order:\n',np.sort(a,axis=None))

#sort array row-wise
print('Row-wise sorted array:\n',np.sort(a,axis=1))

#specify sort algorithm
print('Column-wise sorted array:\n',np.sort(a,axis=0))

dtypes =[('name','S10'),('grade_year',int),('cgpa',float)]

#Values to be put in array
values=[('Hrithik',2009,8.5),('Ajay',2008,8.7),('Pankaj',2008,7.9),('Aakash',2009,9.0)]

arr=np.array(values,dtype=dtypes)
print('\nArray sorted by names:\n',np.sort(arr,order='name'))

print('Array sorted by graduation year and then cgpa:\n',np.sort(arr,order=['grade_year','cgpa']))


