import math
V = float(input("ingrese la velocidad:"))
ang = float(input("ingrese el angulo:"))
y = 1
t = 1
g = 9.8
ag = math.radians(ang)
while y > 0:
    x = V*math.cos(ag)*t
    y = V*math.sin(ag)*-1/2*g*t**2
    t = t+1
    print(x, y)
