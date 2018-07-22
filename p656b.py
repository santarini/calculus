from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np


fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

ax = plt.axes(projection='3d')

#domain
#zline = np.linspace(0, 15, 1000)
t=np.linspace(0, 15, 1000)

#equations
xline = np.cos(t)
yline = np.sin(t)
zline = np.sin(2*t)
ax.plot3D(xline, yline, zline, color='gray')

#axis labels
ax.set_xlabel('X axis')
ax.set_ylabel('Y axis')
ax.set_zlabel('Z axis')

plt.show()
