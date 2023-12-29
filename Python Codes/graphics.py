import json
from math import atan, cos, sqrt
from matplotlib import pyplot as plt
from numpy import arange
R_kerbin = 600000

plt.style.use('grayscale')

with open('data.txt', 'r') as fr:   # Читаем данные с прошлых этапов
    PastValues = json.load(fr)

def Correction(x, y):
    h = R_kerbin * (1 / cos(atan(x / R_kerbin)) - 1)
    return y + h

x = [Correction(x[-1][0], x[-1][1]) for x in PastValues]
y = [x[-1][0] for x in PastValues]
a = [sqrt(a[0][1] ** 2 + a[0][0] ** 2) for a in PastValues]
v = [sqrt(v[1][1] ** 2 + v[1][0] ** 2) for v in PastValues]

plt.rcParams['font.size'] = 7

t = list(arange(0.0, 410.01, 0.01))
print(len(t))
print(len(a))
plt.subplot(2, 1, 1)
plt.plot(t, a)
plt.title("Ускорение(t)")

plt.subplot(2, 2, 3)
plt.plot(t, y)
plt.title("Высота(t)")

plt.subplot(2, 2, 4)
plt.plot(t, v)
plt.title("Скорость(t)")

plt.show()
