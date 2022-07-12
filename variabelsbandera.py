import random


def generaraleatorios(cantidad, limite):
    milista = []
    for _ in range(0, cantidad):
        milista.append(random.randint(0, limite))
    return milista


lista = generaraleatorios(100, 1000)
sorted(lista)
n = float(input("ingrese el numero:"))
bandera = False
for x in lista:
    if x % n == 0:
        bandera = True
        break

if bandera == True:
    print(x)
    print("eureka")
