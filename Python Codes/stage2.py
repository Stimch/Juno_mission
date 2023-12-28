from math import *
from matplotlib import pyplot as plt
import json

with open('data.txt', 'r') as file_in:
    PastValues = json.load(file_in)

density0 = 1.225
e = 2.7128
Mmol = 0.029
R = 8.31
T_air = 290

g = 9.80665 #
S = 10.3 ** 2 * pi / 4
m0 = 33000
c = 0.03
flight_time_2 = 184
angle_new = (17 * pi / 180) / flight_time_2 #
angle_past = 61 * pi / 180 #
angle = (78 * pi / 180) / flight_time_2 #

Ft2_max = 94
Ft2_min = 80.8

F = (Ft2_max * 4) * 9800
F_min = (Ft2_min * 4) * 9800
F_increase = (F - F_min) / flight_time_2
m_release = 310.0

hundredth = 0.01

speed_x = PastValues[-1][1][0]
speed_y = PastValues[-1][1][1]
coord_y = PastValues[-1][2][1]
print(len(PastValues))

def p_env(h):
    return density0 * e**((-Mmol * h * g) / (R * T_air))

def F_Resistance(v, h):
    return (c * S * p_env(h) * (v ** 2)) / 2

def acceleration_x(t, v, h):
    return ((F_min + F_increase * t) * sin(angle * t) - F_Resistance(v, h)) / (m0 - m_release * t)

def acceleration_y(t):
    return ((F_min + F_increase * t) * cos(angle * t)) / (m0 - m_release * t) - g

def Euler(x, y):
    return x + 2 * hundredth * y

def getValues(PastValues, flight_time):
    global speed_x
    global speed_y
    global coord_y
    for i in range(int(flight_time / hundredth)):
        acc_x = acceleration_x(hundredth * i, speed_x, coord_y)
        speed_x = Euler(PastValues[-1][1][0], acc_x)
        coord_x = Euler(PastValues[-1][2][0], PastValues[-1][1][0])
        acc_y = acceleration_y(hundredth * i)
        speed_y = Euler(PastValues[-1][1][1], acc_y)
        coord_y = Euler(PastValues[-1][2][1], PastValues[-1][1][1])
        PastValues.append([[acc_x, acc_y], [speed_x, speed_y], [coord_x, coord_y]])

getValues(PastValues, flight_time_2)
for i in PastValues:
    print(i)


with open('data.txt', 'w') as file_out:
    json.dump(PastValues, file_out)
