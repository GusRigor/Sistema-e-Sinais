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

def i(t, i0):
    return i0 * exp(-t/(r*c*0.5))

while graphT[-1] < n:
    graphT.append(graphT[-1]+h)
    
    k1= i(graphT[-1], graphI[-1])
    k2= i(graphT[-1] + h/2, graphI[-1] + h/2)
    k3= i(graphT[-1] + h/2, graphI[-1]+ (h/2)*k2)
    k4= i(graphT[-1]+ h, graphI[-1]+ h*k3)

    graphI.append(graphI[-1] + (h/6)*(k1 + 2*k2 + 2*k3 + k4))

plt.plot(graphT,graphI, label='i(t)')
plt.legend()
plt.show()  