import matplotlib
from pylab import *
import numpy as np

x = linspace(0, 10, 100)

y = sin(x)/x
plt.subplot(1, 3, 1)
plt.plot(x, y)

y = 1 - x**2/6
plt.subplot(1, 3, 2)
plt.plot(x, y)

y = 1 - x**2/6 + x**4/120
plt.subplot(1, 3, 3)
plt.plot(x, y)



plt.show()

input('Enter any key to continue')

fig = figure()
ax = fig.add_subplot(111, projection='3d')

xk = int(input('kf for x\n'))
yk = int(input('kf for y\n'))
zk = int(input('kf for z\n'))

u = linspace(0, 2 * pi, 100)
v = linspace(0, pi, 100)

x = xk * outer(cos(u), sin(v))
y = yk * outer(sin(u), sin(v))
z = zk * outer(ones_like(u), cos(v))

ax.plot_surface(x, y, z)

show()