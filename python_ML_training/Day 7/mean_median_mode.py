import numpy as np
from scipy import stats

speed = [99,86,88,111,86,103,87,94,78,77,85,86]


x= np.mean(speed)

print('mean of speed',x)

x=np.median(speed)
print('median of speed',x)

x=stats.mode(speed)
print('Mode of speed',x)