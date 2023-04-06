import pygame
from pygame.locals import *

pygame.init()

FPS = 60
FramePerSec = pygame.time.Clock()

WINDOW_WIDTH = 400
WINDOW_HEIGHT = 400

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

CURRENT_COLOR = BLACK
ERASER = False

DISPLAYSURF = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Paint")

def draw(surface, color, start, end, width):
    if ERASER:
        draw_circle(surface, WHITE, end, width)
        draw_rectangle(surface, WHITE, (end[0]-width, end[1]-width), (end[0]+width, end[1]+width))
    else:
        pygame.draw.line(surface, color, start, end, width)

def draw_rectangle(surface, color, start_pos, end_pos):
    rect = pygame.Rect(start_pos, end_pos)
    pygame.draw.rect(surface, color, rect)

def draw_circle(surface, color, center, radius):
    pygame.draw.circle(surface, color, center, radius)

def main():
    global CURRENT_COLOR
    drawing = False
    radius = 1
    last_pos = (0, 0)
    width = 1

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()

            if event.type == MOUSEBUTTONDOWN:
                drawing = True
                last_pos = event.pos

            if event.type == MOUSEMOTION and drawing:
                draw(DISPLAYSURF, CURRENT_COLOR, last_pos, event.pos, width)
                last_pos = event.pos

            if event.type == MOUSEBUTTONUP:
                drawing = False

            if event.type == KEYDOWN:
                if event.key == K_r:
                    CURRENT_COLOR = RED
                elif event.key == K_g:
                    CURRENT_COLOR = GREEN
                elif event.key == K_b:
                    CURRENT_COLOR = BLUE
                elif event.key == K_k:
                    CURRENT_COLOR = BLACK
                elif event.key == K_e:
                    ERASER = not ERASER
                    if ERASER:
                        width = 10
                    else:
                        width = 1

        pygame.display.update()
        FramePerSec.tick(FPS)

if __name__ == '__main__':
    main()
