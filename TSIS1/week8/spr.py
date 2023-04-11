import pygame
from ball import Ball
pygame.init()

W, H = 618, 359 

screen = pygame.display.set_mode((W,H))
clock = pygame.time.Clock()
FPS = 60
speed = 3
balls = pygame.sprite.Group()
balls.add(Ball(W//2, speed ,'images/Coin.png'),
          Ball(W//2-100, 3, 'images/cn1.png'),
          Ball(W//2+100, 2, 'images/cn2.png'),
          Ball(W//2-250, 4, 'images/star.png'))
bg = pygame.image.load('images/bg.png').convert_alpha()
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
            
    screen.blit(bg,(0,0))
    balls.draw(screen)
    pygame.display.update()
    clock.tick(FPS)
    balls.update(H)
    

