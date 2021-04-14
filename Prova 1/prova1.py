#Prova 1 - The Twin Capacitor Paradox - Gustavo G. Rigor - BEC VII

import matplotlib.pyplot as plt
from math import exp

r = float(input('Valor de R(ohms): '))
c = float(input('Valor de C(Farads): '))
v0 = float(input('Valor inicial da tensão no capacitor(Volts): '))

graphT = []
graphI = []
graphV = []
graphV1 = []
graphV2 = []

t0 = 0
i0 = v0/r
v10 = v0
v20 = 0

graphT.append(t0)
graphI.append(i0)
graphV1.append(v10)
graphV2.append(v20)
graphV.append(v0)

h = 0.1
n = 2.5/h

def v(t):
    return v0 * exp(-t*2/(r*c))

def i(i0, t):
    return i0 * exp(-t/(r*c*0.5)) 

def v1(v):
    return 0.5*(v0 + v)

def v2(v):
    return 0.5*(v0 - v)

while graphT[-1] < n:
    graphT.append(graphT[-1]+h)
    graphI.append(i(graphI[-1],graphT[-1]))
    graphV.append(v(graphT[-1]))
    graphV1.append(v1(graphV[-1]))
    graphV2.append(v2(graphV[-1]))

plt.plot(graphT,graphV1, label='v1(t)')
plt.plot(graphT,graphV2, label='v2(t)')
plt.plot(graphT,graphV, label='v(t)')
plt.plot(graphT,graphI, label='i(t)')
plt.legend()
plt.show()   