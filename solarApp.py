import math
from bigfloat import *
import matplotlib.pyplot as plt
from visual import *


# A class to handle the time ranges
class timeHoursSeconds(object):
    def __init__(self, s, h, d, y):
        self.s = s
        self.h = h
        self.d = d
        self.y = y

    def fromStoHours(self):
        h = self.s / 60 / 60
        return h

    def fromStoDays(self):
        d = self.s / 60 / 60 / 24
        return d

    def fromStoYears(self):
        y = self.s / 60 / 60 / 24 / 365
        return y

    def fromDaysToS(self):
        s = self.d * 24 * 60 * 60
        return s

    def fromDaysToH(self):
        h = self.d * 24
        return h

    def fromDaysToY(self):
        y = self.d / 365
        return y


class planet(object):
    G = 6.67 * math.pow(10, -11)
    sunM = 1.989 * math.pow(10, 30)
    eaM = 5.973 * math.pow(10, 24)
    RTL = 384400000

    def __init__(self, name, mass, RS, theta0, radius):
        self.name = name
        self.mass = mass
        self.RS = RS
        self.theta0 = theta0
        self.radius = radius

    def gravitationalForce(self, m2=1):
        if m2 == 1:
            f = self.G * (self.mass * self.sunM) / math.pow(self.RS, 2)
        else:
            f = self.G * (self.mass * self.eaM) / math.pow(self.RTL, 2)
        return f

    def angularVelocity(self, m2=1):
        w = math.sqrt(self.gravitationalForce(m2=m2) / (self.mass * self.RS))
        return w

    def velocity(self, m2=1):
        v = self.angularVelocity(m2=1) * self.RS
        return v

    def angularPosition(self, t, m2=1):
        theta = self.theta0 + self.angularVelocity(m2=m2) * t
        return theta

    def varAngularPosition(self, t, dt, m2=1):
        dtheta = self.angularPosition(t + dt, m2=m2) - self.angularPosition(t, m2=m2)
        return dtheta

    def periodAroundSun(self, m2=1):
        p = timeHoursSeconds(2 * math.pi / self.angularVelocity(m2=m2), 0, 0, 0)
        return p

    def picture(self, x, y, z, col, trail):
        if col == 1:
            return sphere(pos=vector(x, y, z), color=color.red, radius=self.radius, make_trail=trail)
        elif col == 2:
            return sphere(pos=vector(x, y, z), color=color.blue, radius=self.radius, make_trail=trail)
        elif col == 3:
            return sphere(pos=vector(x, y, z), color=color.green, radius=self.radius, make_trail=trail)
        elif col == 4:
            return sphere(pos=vector(x, y, z), color=color.cyan, radius=self.radius, make_trail=trail)
        elif col == 5:
            return sphere(pos=vector(x, y, z), color=color.yellow, radius=self.radius, make_trail=trail)
        else:
            return sphere(pos=vector(x, y, z), color=color.white, radius=self.radius, make_trail=trail)


mercury = planet("Mercury", 3.302 * math.pow(10, 23), 57910000000, 0, 0.3)
venus = planet("Venus", 4.8685 * math.pow(10, 24), 108200000000, 0, 0.4)

earth = planet("Earth", 5.973 * math.pow(10, 24), 149600000000, 0, 0.5)
# As for the Moon, input Earth-Moon distance
moon = planet("Moon", 7.347 * math.pow(10, 22), 384400000, 0, 0.2)

mars = planet("Mars", 6.4185 * math.pow(10, 23), 227900000000, 0, 0.45)
jupiter = planet("Jupiter", 1.8986 * math.pow(10, 27), 778500000000, 0, .8)
saturn = planet("Saturn", 5.6846 * math.pow(10, 26), 1433000000000, 0, 0.7)
uranus = planet("Uranus", 8.6832 * math.pow(10, 25), 2877000000000, 0, 0.6)
neptune = planet("Neptune", 1.0243 * math.pow(10, 26), 4503000000000, 0, 0.6)

# Simulation data
years = timeHoursSeconds(0, 0, 3655, 0)
seconds = years.fromDaysToS()
print("Years: ", years.y)
print("Days: ", years.d)
print("Seconds: ", seconds)
t = 0
dt = timeHoursSeconds(10000, 0, 0, 0)

# Planets
merc = mercury.picture(1.5, 0, 0, 1, True)
ven = venus.picture(3, 0, 0, 3, True)
ea = earth.picture(5, 0, 0, 2, True)
mar = mars.picture(7, 0, 0, 3, True)
jup = jupiter.picture(9, 0, 0, 5, True)
sat = saturn.picture(11, 0, 0, 6, True)
ur = uranus.picture(13, 0, 0, 3, True)
nep = neptune.picture(15, 0, 0, 2, True)
planetsf = [merc, ven, ea, mar, jup, sat, ur, nep]
planets = [mercury, venus, earth, mars, jupiter, saturn, uranus, neptune]
# The Moon
v = vector(0.9, 0, 0)
mo = moon.picture(5 + 0.9, 0, 0, 10, True)

for k in planets:
    revp = k.periodAroundSun()
    print("Planet name: ", k.name)
    print(k.name, " mass: ", k.mass, " kg")
    print(k.name, " distance from the sun: ", k.RS / 1000, " Km")
    print(k.name, " angular velocity: ", k.angularVelocity(), " rad/s")
    print(k.name, " period around the sun: ", revp.fromStoYears(), " terrestrial year/s")
    print("\n")

# Our program
while t < seconds:
    rate(50)
    for plan in range(len(planets)):
        planetsf[plan].pos = rotate(planetsf[plan].pos, angle=planets[plan].varAngularPosition(t, dt.s), axis=(0, 0, 1))
    v = rotate(v, angle=moon.varAngularPosition(t, dt.s, m2=2), axis=(0, 0, 1))
    mo.pos = ea.pos + v
    t += dt.s