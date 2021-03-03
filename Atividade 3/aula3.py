#exemplo de aplicacao de integracao numerica Runge Kutta
import math
import matplotlib.pyplot

R = int(input('Resistência (ohms): '))
L = float(input('Indutância (Henrys): '))
C = float(input('Capacitância (Farads): '))



X = 10.0
Y = 0.0
Z = 0.1

h = 0.001
T = 0


rk11 = 0
rk12 = 0
rk13 = 0
rk14 = 0

rk21 = 0
rk22 = 0
rk23 = 0
rk24 = 0

def kUm1(z):
    return z

def kDois1(z, k1):
    return z + k1 * h/2

def kTres1(z, k2):
    return z + k2 * h/2

def kQuatro1(z, k3):
    return z + k3 * h

def kUm2(z, y):
    return ((- R/L) * z) - ( 1/(L*C) * y)

def kDois2(z, y, k1):
    return ((- R/L) * z) - ( 1/(L*C) * y) + k1 * h/2

def kTres2(z, y, k2):
    return ((- R/L) * z) - ( 1/(L*C) * y) + k2 * h/2

def kQuatro2(z, y, k3):
    return ((- R/L) * z) - ( 1/(L*C) * y) + k3 * h

def z2y(z0, z1):
    return (z1 - z0)/h 

graphT = []
graphX = []
graphY = []

while T < 1:
    
    rk11 = kUm1(Z)
    rk21 = kUm2(Z, Y)

    rk12 = kDois1(Z, rk11)
    rk22 = kDois2(Z, Y, rk21)

    rk13 = kTres1(Z, rk12)
    rk23 = kTres2(Z, Y, rk22)

    rk14 = kQuatro1(Z, rk13)
    rk24 = kQuatro2(Z, Y, rk23)

    graphT.append(T)
    graphX.append(X)

    aZ = Z + (rk11 + 2 * rk12 + 2 * rk13 + rk14)/6
    graphY.append(z2y(Z, aZ))
    Z = aZ

    Y = Y + (rk21 + 2 * rk22 + 2 * rk23 + rk24)/6
    T = T + h

matplotlib.pyplot.plot(graphT,graphX,label='x(t)')
matplotlib.pyplot.plot(graphT,graphY,label='y(t)')
matplotlib.pyplot.xlabel('tempo (t)')
matplotlib.pyplot.ylabel('valores (x e y)')
matplotlib.pyplot.title('Exercício Aula 3 - Gustavo R. BEC')
matplotlib.pyplot.legend()
matplotlib.pyplot.show()