from SteadyAircraftFlight import standard_atmosphere
import matplotlib.pyplot as plt

temperature = []
pressure = []
density = []
altitude = []
for h in range(0, 90000, 100):
    t, p, rho = standard_atmosphere(h)
    temperature.append(t - 459.67)
    pressure.append(p)
    density.append(rho * 1000)
    altitude.append(h / 10000)

fig, subplot = plt.subplots(1, 3, figsize=(12, 4), sharey=True)
subplot[0].plot(temperature, altitude)
subplot[0].set_title('Temperature (F)')
subplot[0].set_ylabel('Altitude (ft * 10^4)')
subplot[0].grid(True)

subplot[1].plot(pressure, altitude)
subplot[1].set_title('Pressure (lbs/ft^2)')
subplot[1].grid(True)

subplot[2].plot(density, altitude)
subplot[2].set_title('Density (slugs/ft^3 * 10^-3)')
subplot[2].grid(True)

# fig.suptitle('Standard Atmospheric Pressure', fontsize=16)
plt.show()
