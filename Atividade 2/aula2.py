########################## Bibliotecas ################################

import matplotlib.pyplot as plt 
from math import e

########################## Funções para o ex ############################

def modulo(x):
    return (x**2)**(1/2)

def energia(deltaT):
    """
    Energia para o gráfico apresentado na pág 8 da segunda aula
    No intervalo de  -10 a 10. 
    """
    TempoAtual = -10
    Energia = 0
    while (TempoAtual < 10):
        if TempoAtual < -1:
            Energia += 0
        elif -1 <= TempoAtual <= 0:
            Energia += (2**2) * deltaT
        else:
            Energia += modulo(2*(e**(-TempoAtual/2))) * deltaT
        
        TempoAtual += deltaT
    print(f'Energia: {Energia}| Esperado: 8| Erro: {modulo(Energia-8)/8 *100}%')

def potencia_RMS(deltaT):
    """
    Potência e valor RMS para o gráfico apresentado na pág 8 da segunda aula
    No intervalo de  -1 a 1. 
    """
    TempoAtual = -1
    Potencia = 0

    while (TempoAtual < 1):
        Potencia += (modulo(TempoAtual)**2) * deltaT
        TempoAtual += deltaT
    print(f'Potência: {Potencia/2} | Esperado: 1/3| Erro: {modulo((Potencia/2)-(1/3))/(1/3) *100}%')
    print(f'Valor RMS: {((Potencia/2)**(1/2))} | Esperado: 1/sqrt(3)| Erro: {modulo(((Potencia/2)**(1/2))-(1/(3**(1/2))))/(1/(3**(1/2))) *100}%')

def main():
    passo = float(input('Defina o tamanho do passo delta t: '))

    if passo < 0:
        passo = passo * -1

    energia(passo)
    potencia_RMS(passo)

repetir = True

while repetir:
    main()
    repetir =  True if input('Repetir para outro delta T? [S/N] ') == 'S' else False