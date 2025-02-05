import pandas as pd

data={
    'calories':[420,380,390],
    'duration':[50,40,45]

}

myvar=pd.DataFrame(data)

print('Values =\n',myvar)

#locate Row
print('Located Row 0\n',myvar.loc[0])

#use a lit of indexes:

print('List of Indexes: \n',myvar.loc[[0,1]])