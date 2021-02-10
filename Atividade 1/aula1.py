import matplotlib.pyplot as plt

tempo = []
x1 = []
for t in range(0, 21):
    tempo.append(t/10)
    x1.append(t*10)

plt.ioff()

plt.plot(tempo,x1,label='x1')
plt.xlabel('tempo (t)')
plt.ylabel('valores (x1)')
plt.title('Exercício Runge-Kutta graph - Gustavo R. BEC')
plt.legend()
plt.show()