import pandas as pd
calories={'day1':420, 'day2':380,'day3':390}

myvar=pd.Series(calories)

print('values\n',myvar)

#example 2
myvar=pd.Series(calories,index=['day1','day2'])

print('value 2\n',myvar)