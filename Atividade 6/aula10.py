import matplotlib.pyplot as plt

def verifica_entrada(str,*args):
    entrada = input(str).upper()
    for x in args:
        if x == entrada:
            return entrada
    print('Entrada inválida. Insira novamente um dos comandos.')
    return verifica_entrada(str,args)    

def verifica_entrada_num(str):
    entrada = input(str)
    if any(chr.isdigit() for chr in entrada):
        return float(entrada)
    print('Entrada inválida. Insira novamente um valor válido.')
    return verifica_entrada_num(str) 

def plot_grafico(t,x,y, delta_t):
    plt.subplot(2,2,1)
    plt.plot(t, x, label='x(t)')
    plt.legend()
    plt.subplot(2,2,2)
    plt.stem(t,x, label='x(T)')
    plt.legend()
    plt.subplot(2,2,3)
    plt.stem(t,y, label='y(T)')
    plt.legend()
    plt.subplot(2,2,4)
    plt.plot(t, y, label='y(t)')
    plt.legend()
    plt.show()


r_or_p = True if "R"==verifica_entrada('Reta ou Parábola? [R/P]','R', 'P') else False


if r_or_p:
    print('Você selecionou RETA, insira os valores de A e B ( y(x) = Ax + B )')
    a = verifica_entrada_num('Insira o valor de A: ')
    b = verifica_entrada_num('Insira o valor de B: ')
    Tm = verifica_entrada_num('Insira o valor de T mín [coloque 0 para o valor padrão]: ')
    T = verifica_entrada_num('Insira o valor de T máx [coloque 0 para o valor padrão]: ')
    T = 2 if T==0 else T
    delta_t = verifica_entrada_num('Insira o valor de delta t [coloque 0 para o valor padrão]: ')
    delta_t = 0.5 if delta_t==0 else delta_t
    t = [Tm]
    x = [a*t[-1] + b]
    y = [0]

    while t[-1] <= T:
        t.append(t[-1]+delta_t)
        x.append(a*t[-1] + b)
        y.append((x[-1] - x[-2])/delta_t)

    plot_grafico(t,x,y,delta_t)
else:
    print('Você selecionou PARÁBOLA, insira os valores de A, B e C ( y(x) = Axˆ2 + Bx + C )')
    a = verifica_entrada_num('Insira o valor de A: ')
    b = verifica_entrada_num('Insira o valor de B: ')
    c = verifica_entrada_num('Insira o valor de C: ')
    Tm = verifica_entrada_num('Insira o valor de T mín [coloque 0 para o valor padrão]: ')
    T = verifica_entrada_num('Insira o valor de T máx[coloque 0 para o valor padrão]: ')
    T = 2 if T==0 else T
    delta_t = verifica_entrada_num('Insira o valor de delta t [coloque 0 para o valor padrão]: ')
    delta_t = 0.05 if delta_t==0 else delta_t
    t = [Tm]
    x = [a*t[-1]*t[-1] + b*t[-1] + c]
    y = [0]

    while t[-1] <= T:
        t.append(t[-1]+delta_t)
        x.append(a*t[-1]*t[-1] + b*t[-1] + c)
        y.append((x[-1] - x[-2])/delta_t)

    plot_grafico(t,x,y, delta_t)

    
