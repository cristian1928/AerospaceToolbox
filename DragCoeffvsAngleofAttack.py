import matplotlib.pyplot as plt
import numpy as np
a = np.linspace(0, 23.2, 500)
cl0, cla, cd0, k = 0.02, 0.12, 0.015, 0.05
cl = cl0 + (cla*a)
cd = cd0 + (k * cl**2)

plt.plot(a, cd)
plt.ylabel('Drag Coefficient')
plt.xlabel('Angle of Attack (degrees)')
plt.title('Dependence of drag coefficient on angle of attack')
plt.grid(True)

plt.show()
