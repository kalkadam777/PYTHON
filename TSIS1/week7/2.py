import pygame
pygame.init()

pygame.display.set_mode((600,400),pygame.RESIZABLE)



white = (255,255,255)
sc = pygame.display.set_mode((600,400), pygame.RESIZABLE)  
pygame.draw.rect(sc, white, (10,10,50,100))

pygame.display.flip()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()