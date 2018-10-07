import SteadyAircraftFlight
import numpy as np
import matplotlib.pyplot as plt
import csv
from math import pi

epsilon = 0.75          # oswald efficiency factor
m = 0.6                 # 0.6 assumption pg. 48
c_d_nought = 0.01277

new_aircraft_array = []
new_velocity_array = []
new_thrust_array = []
new_throttle_setting = []

with open('data.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    aircraft_array = []
    wingspan_array = []
    surface_area_array = []
    max_takeoff_array = []
    max_thrust_array = []
    flight_ceiling_array = []
    y_n = []

    for row in readCSV:
        aircraft_1 = row[0]
        wing = float(row[1])
        sa = float(row[2])
        mto = float(row[3])
        mt = float(row[4])
        fc = float(row[5])
        yes_or_no = row[6]

        aircraft_array.append(aircraft_1)
        wingspan_array.append(wing)
        surface_area_array.append(sa)
        max_takeoff_array.append(mto)
        max_thrust_array.append(mt)
        flight_ceiling_array.append(fc)
        y_n.append(yes_or_no)


for i in range(0, 15):

    aircraft = aircraft_array[i]
    wingspan = wingspan_array[i]
    surface_area = surface_area_array[i]
    max_takeoff_weight = max_thrust_array[i]
    max_thrust = max_thrust_array[i]
    flight_ceiling = flight_ceiling_array[i]

    k = 1 / (pi * epsilon * ((wingspan ** 2) / surface_area))

    temp, pres, dens = SteadyAircraftFlight.standard_atmosphere(flight_ceiling)
    min_v = round(np.real(SteadyAircraftFlight.min_airspeed(max_takeoff_weight, dens, surface_area, k, c_d_nought)), 2)
    thrust_req = round(np.real(SteadyAircraftFlight.thrust_required(max_takeoff_weight, c_d_nought, k)), 2)
    throttle_s = round(np.real(SteadyAircraftFlight.throttle_setting(thrust_req, max_thrust, m, dens)), 2)

    new_aircraft_array.append(aircraft)
    new_velocity_array.append(min_v)
    new_thrust_array.append(thrust_req)
    new_throttle_setting.append(throttle_s)


fig, subplot = plt.subplots(3, 1, figsize=(16, 8), sharex=True)
subplot[0].scatter(new_aircraft_array, new_velocity_array)
subplot[0].set_ylabel('Stall Velocity (ft/s)')
subplot[0].grid(True)

subplot[1].scatter(new_aircraft_array, new_thrust_array)
subplot[1].set_ylabel('Minimum Thrust Required (lbs)')
subplot[1].grid(True)

subplot[2].scatter(new_aircraft_array, new_throttle_setting)
subplot[2].set_ylabel('Throttle Setting')
subplot[2].set_xlabel('Aircraft Model')
subplot[2].grid(True)

plt.subplots_adjust(wspace=None, hspace=None)

# plt.savefig('Plot')
plt.show()
