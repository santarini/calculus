#! python3
#graph of r(t) = cos(t)i + sin(t)j + sin(2t)k

from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

ax = plt.axes(projection='3d')

t=np.linspace(0, 15, 1000)

xline = np.cos(t)
yline = np.sin(t)
zline = np.sin(2*t)
ax.plot3D(xline, yline, zline, 'gray')

plt.show()
