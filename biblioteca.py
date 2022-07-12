import pygame

pygame.init()
screen = pygame.display.set_mode((700, 700))
myclock = pygame.time.Clock()

blanco = (255, 255, 255)

i = 0
j = 100

bandera = 'crecer'
while True:
    screen.fill(blanco)
    pygame.draw.circle(screen, (250, 0, 250), (450, 450), i)

    pygame.draw.circle(screen, (0, 250, 0), (100, 100), j)
    if i == 0:
        bandera = 'crecer'
    if i == 200:
        bandera = 'decrecer'
    if bandera == 'crecer':
        i = i+1
    else:
        i = i-1
    if j == 0:
        bandera = 'decrecer'
    if j == 200:
        bandera = 'crecer'
    if bandera == 'decrecer':
        j = j+1
    else:
        j = j-1
    pygame.display.update()
    myclock.tick(100)
