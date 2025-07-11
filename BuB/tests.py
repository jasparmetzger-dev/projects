import numpy as np
import matplotlib.pyplot as plt

def parabel_wurf(x, theta, g, v_0):
    rad = np.deg2rad(theta) # wir müssen einmal von Grad zu Bogenmaß wechseln
    return float(x*np.tan(rad) - g*x**2 / (2*v_0**2 * np.cos(rad)**2))

winkel = 40
g = 9.81
v_0 = 10
hoehen = []
x_vals = []

for x in range(20):
    x_vals.append(x/2)
    hoehen.append(parabel_wurf(x/2, winkel, g, v_0))
print(hoehen)

plt.title('Parabel Wurf')
plt.plot(x_vals, hoehen)
plt.xlabel('Weite')
plt.ylabel('Höhe')

plt.show()