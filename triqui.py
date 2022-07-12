import random
A = ['', '', '']
B = ['', '', '']
C = ['', '', '']
lista = [A,
         B,
         C]
turno = 'X'


def recrrertablero(lista):
    for fila in (lista):
        print(fila)


def cambiodeturno(turno):
    if (turno == 'X'):
        turno = 'O'
    else:
        turno = 'X'
    return turno


def jugar(lista, turno):
    if turno == 'X':
        X = int(input("ingrese posicion x:"))
        Y = int(input("ingrese posicion Y:"))
        lista[X][Y] = turno
        recrrertablero(lista)
        print("//////////////")
    else:
        X = random.randint(0, 2)
        Y = random.randint(0, 2)
        if lista[X][Y] == '':
            lista[X][Y] = turno
            recrrertablero(lista)
        else:
            jugar(lista, turno)


for jugada in range(0, 18):
    if A == ['X', 'X', 'X'] or B == ['X', 'X', 'X'] or C == ['X', 'X', 'X'] or A[0] == 'X' and B[0] == 'X' and C[0] == 'X' or A[1] == 'X' and B[1] == 'X' and C[1] == 'X' or A[2] == 'X' and B[2] == 'X' and C[2] == 'X' or A[0] == 'X' and B[1] == 'X' and C[2] == 'X' or A[2] == 'X' and B[1] == 'X' and C[0] == 'X':
        print("Gano")
        break
    if A == ['O', 'O', 'O'] or B == ['O', 'O', 'O'] or C == ['O', 'O', 'O'] or A[0] == 'O' and B[0] == 'O' and C[0] == 'O' or A[1] == 'O' and B[1] == 'O' and C[1] == 'O' or A[2] == 'O' and B[2] == 'O' and C[2] == 'O' or A[0] == 'O' and B[1] == 'O' and C[2] == 'O' or A[2] == 'O' and B[1] == 'O' and C[0] == 'O':
        print("Perdio")
        break
    jugar(lista, turno)
    turno = cambiodeturno(turno)
