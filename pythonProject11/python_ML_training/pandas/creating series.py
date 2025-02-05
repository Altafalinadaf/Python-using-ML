import pandas as pd
import numpy as np

#creating empty series

ser = pd.Series()
ser1 = pd.Series(5)

print(ser)
print(ser1)

#simple array
data =np.array(['p','y','t','h','o','n'])

ser =pd.Series(data)
print(ser)
#example 2
a=[1,7,2]
myvar=pd.Series(a)
print('Series 2\n',myvar)
print('Accessed',myvar[0])