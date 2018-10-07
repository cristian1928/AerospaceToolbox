from math import exp, sqrt


def standard_atmosphere(height):                 # pg. 14, works
    height = float(height)
    # Standard Atmosphere
    # Input: h altitude (ft)
    # Output: t Temperature (F), p pressure (lbs/ft^2), rho density (slug/ft^3)

    h1, h2, h3, a0, a2, g, r = 3.6089e4, 6.5616e4, 9.0e4, -3.567e-3, 5.494e-4, 32.2, 1716
    t0, p0, rho0 = 518.67, 2116.2, 2.3769e-3

    t1 = t0 + a0*h1
    p1 = p0 * (t1/t0)**(-g/a0/r)
    rho1 = rho0 * (t1/t0)**(-g/a0/r-1)
    t2 = t1
    p2 = p1 * exp(-g/r/t2 * (h2-h1))
    rho2 = rho1 * exp(-g/r/t2 * (h2-h1))
    global rho
    if height <= h1:
        # Troposphere
        t = t0 + a0*height
        p = p0 * (t/t0)**(-g/(a0*r))
        rho = rho0 * (t/t0)**(-g/(a0*r) - 1)
        return t, p, rho
    elif height <= h2:
        # Tropopause
        t = t1
        p = p1 * exp((-g/(r*t))*(height-h1))
        rho = rho1 * exp((-g/(r*t)) * (height-h1))
        return t, p, rho
    elif height <= h3:
        # Stratosphere
        t = t2 + a2 * (height-h2)
        p = p2 * (t/t2)**(-g/(a2*r))
        rho = rho2 * (t/t2)**(-g/(a2*r) - 1)
        return t, p, rho
    else:
        print("Error: The altitude should be less than 90'000 ft")
        return 0, 0, 0


def thrust_required(w, cd0, k):              # pg. 103, works correctly
    thrust = 2*w*sqrt(cd0*k)
    return thrust


def min_airspeed(w, dens, s, k, cd0):
    return sqrt((2*w)/(dens*s) * sqrt(k/cd0))


def throttle_setting(min_thrust, m_thrust, m, dens):  # pg. 48
    blah, blah, rhos = standard_atmosphere(0)
    return (min_thrust/m_thrust) * (rhos/dens)**m
