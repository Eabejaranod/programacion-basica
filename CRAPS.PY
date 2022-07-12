import random

print("bienvenido a crapss")
d1 = random.randint(1, 6)
d2 = random.randint(1, 6)
print(d1, d2)
print(d1+d2)
if d1 + d2 == 7 or d1 + d2 == 11:
    resultado = "ganó"
else:
    if d1+d2 == 2 or d1+d2 == 3 or d1+d2 == 12:
        resultado = "pierde"
    else:
        punto = d1+d2
        print("su punto es", d1+d2)
        resultado = "continuar"
while resultado == "continuar":
    d1 = random.randint(1, 6)
    d2 = random.randint(1, 6)
    print("la suma es:", d1+d2)
    if d1+d2 == 7:
        resultado = "ganó"
    else:
        if d1+d2 == punto:
            resultado = "ganó"
        else:
            resultado = "continuar"
print(resultado)
