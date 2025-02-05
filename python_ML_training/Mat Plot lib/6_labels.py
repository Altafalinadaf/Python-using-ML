import matplotlib.pyplot as plt

import numpy as np

x=np.array([80,85,90,95])
y=np.array([240,250,260,453])

plt.plot(x,y)

plt.xlabel('Average Pulse')
plt.ylabel('Calories Burnage')
# plt.show()

#label and title

plt.plot(x,y)
plt.title('Sports Watch Date')
#plt.title("Sports Watch Data",loc ='left')
plt.xlabel('Average Pulse')
plt.ylabel('Calories Burnage')
plt.show()
