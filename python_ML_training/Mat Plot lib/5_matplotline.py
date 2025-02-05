import matplotlib.pyplot as plt

import numpy as np

ypoints=np.array([3,8,1,10])

plt.plot(ypoints,linestyle='dotted',color='red',linewidth='10')
plt.show()

plt.plot(ypoints,ls='dashed',color='green',linewidth='10')
plt.show()

plt.plot(ypoints,ls='solid',color='blue',linewidth='10')
plt.show()

plt.plot(ypoints,ls='dashdot',color='orange',linewidth='10')
plt.show()


#multiple lines

x1=np.array([3,8,1,10])
x2=np.array([6,2,7,11])

plt.plot(x1)
plt.plot(x2)

plt.show()

x1=np.array([0,3,5,9])
y1=np.array([5,6,7,8])
x2=np.array([0,1,2,3])
y2=np.array([6,2,7,11])

plt.plot(x1,y1)
plt.plot(x2,y2)
plt.show()
