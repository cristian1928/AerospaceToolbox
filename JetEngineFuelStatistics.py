import numpy as np
import matplotlib.pyplot as plt
from SteadyAircraftFlight import standard_atmosphere

alt = np.linspace(0, 65000, 500)
tsmax, m, c = 12500, 0.6, -0.69

p = []
fr = []

for i in alt:
    temp, pres, rho = standard_atmosphere(i)
    p.append((rho/0.0023769)**m * tsmax)
    fr.append((rho/0.0023769)**m * tsmax * c)


fig, subplot = plt.subplots(1, 2, figsize=(12, 4))
subplot[0].plot(alt, p)
subplot[0].set_title('(a) Thrust vs altitude')
subplot[0].set_ylabel('Thrust (lbs')
subplot[0].set_xlabel('Altitude (ft)')
subplot[0].grid(True)

subplot[1].plot(alt, fr)
subplot[1].set_title('(b) Fuel consumption rate vs altitude')
subplot[1].set_ylabel('Fuel flow rate (lbs/hr)')
subplot[1].set_xlabel('Altitude (ft)')
subplot[1].invert_yaxis()
subplot[1].grid(True)

plt.show()
