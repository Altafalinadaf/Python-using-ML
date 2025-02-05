import matplotlib.pyplot as plt

import numpy as np
xpoints=np.array([2,4,0,5,7,9,14,10,12,7,2])
ypoints=np.array([0,4,6,6,10,6,6,4,0,2,0])
plt.plot(xpoints,ypoints,color='red',linewidth='3')
plt.title('Star')
plt.show()