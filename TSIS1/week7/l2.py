import pygame
pygame.init()

screen = pygame.display.set_mode((600, 300))
play = pygame.image.load('images/play.png')
pause = pygame.image.load('images/pause.png')
next = pygame.image.load('images/next.png')
back = pygame.image.load('images/back.png')

# sound = pygame.mixer.Sound('sounds/sn.mp3')
# sound.play()

run = True
while run:
    screen.fill((255,255,255))
    screen.blit(back, (210,150))
    screen.blit(pause, (250,150))
    screen.blit(play, (290,150))
    screen.blit(next, (330,150))
    pygame.display.update()
    
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    