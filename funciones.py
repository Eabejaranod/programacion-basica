from math import pi


def F_K():
    print("convertidor de fahrenheit a Kelvin")
    fahrenheit = float(input())
    Kelvin = (fahrenheit + 2298.35)*5/9
    print(f"{fahrenheit}Fª equivalen a {Kelvin}kª ")


def GR_RA():
    print("convertidor de Grados a Radianes")
    Grados = float(input())
    Radianes = Grados * pi/100
    print(f"{Grados}ª equivalen a {Radianes}rad ")


def Gr_ON():
    print("convertidor de Gramos a Onzas")
    Gramos = float(input())
    Onzas = Gramos * 0.0353
    print(f"{Gramos}gr equivalen a {Onzas} onzas ")


def menu():
    print("escoja la conversion: \n1)fahrenheit a kelvin. \n2)De Grados a Rdianes. \n3)De gramos a Onzas. ")
    eleccion = int(input())
    if eleccion == 1:
        F_K()
    elif eleccion == 2:
        GR_RA()
    elif eleccion == 3:
        Gr_ON()
    else:
        print("ingrese una eleccion valida")
        menu()


menu()
valor = float(inpout())
