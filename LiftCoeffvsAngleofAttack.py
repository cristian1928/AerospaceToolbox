import matplotlib.pyplot as plt
import numpy as np
a = np.linspace(0, 23.2, 500)
cl0, cla = 0.02, 0.12
cl = cl0 + (cla*a)

plt.plot(a, cl)
plt.ylabel('Lift Coefficient')
plt.xlabel('Angle of Attack (degrees)')
plt.title('Dependence of lift coefficient on angle of attack')
plt.grid(True)

plt.show()
