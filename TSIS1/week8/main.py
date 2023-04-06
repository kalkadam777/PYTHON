import pygame
pygame.init()

W, H = 600, 400
clock = pygame.time.Clock()
FPS = 60
screen = pygame.display.set_mode((W,H))
pygame.display.set_caption('RPG')

x = W // 2
y = H // 2
speed = 5

sp = None
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    # keys = pygame.key.get_pressed()
    
    # if keys[pygame.K_LEFT]:
    #     x -= speed
    # elif keys[pygame.K_RIGHT]:
    #     x += speed
    pressed = pygame.mouse.get_pressed()
    if pressed[0]:
        pos = pygame.mouse.get_pos()
        
        if sp is None:
            sp = pos
            
        width = pos[0] - sp[0]
        height = pos[1] - sp[1]
        
        screen.fill((255,255,255))                
        
        pygame.draw.rect(screen, (65, 105, 225), (sp[0], sp[1], width, height))
        pygame.display.update()
    
    else:
        sp = None
    
    
    clock.tick(FPS)