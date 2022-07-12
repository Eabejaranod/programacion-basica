import random
import numpy as np


def crear_tablero():
    numeros = []
    letras = ['B', 'I', 'N', 'G', 'O']
    rangos = {
        'B': [1, 15],
        'I': [16, 30],
        'N': [31, 45],
        'G': [46, 60],
        'O': [61, 75]
    }

    for i in range(75):
        numeros.append(i+1)

    tablero = []

    for letra in letras:
        lista = []
        while len(lista) < 5:
            numero = random.randint(rangos[letra][0], rangos[letra][1])
            if not numero in lista:
                lista.append(numero)
            if letra == 'N' and len(lista) == 2:
                lista.append(-1)
        tablero += lista

    return tablero


def pintar_tablero(tablero):
    cont = 0
    matris = []
    for i in range(5):
        inico = i*5
        final = (i+1)*5
        lista = tablero[inico:final]
        matris.append(lista)

    # sacado de internet
    np_martis = np.array(matris)
    np_martis = np_martis.transpose()
    print('////////////////////////')
    for line in np_martis:
        print('  '.join(map(str, line)))


def iniciar():
    tablero = crear_tablero()
    #tablero = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25]
    tablero_control = tablero.copy()
    pintar_tablero(tablero)
    while sum(tablero_control) > 0:
        print('Ingrese la balota:')
        valor = input()
        if valor.isnumeric():
            if int(valor) in tablero_control:
                indice = tablero_control.index(int(valor))
                tablero_control[indice] = 0
                tablero[indice] = 'X'
            pintar_tablero(tablero)


iniciar()
