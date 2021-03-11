from math import log, cos, sin, e, pi
# Verificando o númericamente o resultado das convoluções
# h(t) = eˆ(-alfa*t), inversa h(t-tal) =  ln(t)
# x(t) = sen(beta*t)
# y(t) = Integral{ x(tal) * h(t-tal) dtal }

t_ini = 0.000000000000000000000000000001
t_fin = 2
n_trp = 100
t_pas = (t_fin - t_ini) / n_trp
t_atual = t_ini

alfa = -2
beta =  3

def h_t_tal(t):
    return log(-alfa*t)

#print(h_t_tal(1/2*(-1)))

def x_tal(t, degree = True):
    return sin(beta*t*pi/180) if degree else sin(beta*t)

#print(x_tal(30))

def conv(t, degree = True):
    return x_tal(t, degree) * h_t_tal(t)

#print(conv(1))

def p_integral(t, t1, degree = True):
    return (conv(t, degree) + conv(t1, degree)) * t_pas/2
 
resultado = 0
while t_atual < t_fin:
    #print(t_atual)
    t_temp = t_atual
    t_atual += t_pas
    resultado += p_integral(t_temp, t_atual)

print(resultado)
