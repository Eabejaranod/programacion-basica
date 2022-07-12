lista = [3.8, 7.19, 6.4, 3.2, 8.9, 11.3, 14.8, 17.1]
for z in lista:
    print(z)
suma = 0
for z in lista:
    suma = (suma)+z
print("la sumatoria de los valores de la lista es :", suma)
multi = 1
for z in lista:
    multi = (multi*z)
print("la multiplicatoria de los valores de la lista es de :", multi)
menor = 1000
for z in lista:
    if z < menor:
        menor = z
print("el menor numero dentro del arreglo es de: ", menor)
mayor = 15
for z in lista:
    if z > mayor:
        mayor = z
print("el mayor numero dentro del arreglo es de: ", mayor)
