import  pygame
pygame.init()

size = WIDTH, HEIGHT = 640, 320
speed = [1, 1]
BLACK = (0, 0, 0)

screen = pygame.display.set_mode(size)

ball = pygame.image.load("intro_ball.gif")
ballrect = ball.get_rect()
clock = pygame.time.Clock()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    ballrect = ballrect.move(speed)
    if ballrect.left < 0 or ballrect.right > WIDTH:
        speed[0] = -speed[0]
    if ballrect.top < 0 or ballrect.bottom > HEIGHT:
        speed[1] = -speed[1]

    screen.fill(BLACK)
    screen.blit(ball, ballrect)
    
    pygame.display.flip()
    clock.tick(120)
    