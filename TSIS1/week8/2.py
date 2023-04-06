import pygame
import random

# Инициализируем Pygame
pygame.init()

# Определяем константы цветов
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Определяем константы для размеров экрана и сетки
SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480
GRID_SIZE = 10

# Создаем окно
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Задаем заголовок окна
pygame.display.set_caption("Змейка на Pygame")

# Функция для рисования змейки
def draw_snake():
    for segment in snake_segments:
        pygame.draw.rect(screen, GREEN, (segment[0], segment[1], GRID_SIZE, GRID_SIZE))

# Функция для перемещения змейки
def move_snake():
    # Создаем новый сегмент для головы змейки
    head = list(snake_segments[-1])
    if snake_direction == "right":
        head[0] += GRID_SIZE
    elif snake_direction == "left":
        head[0] -= GRID_SIZE
    elif snake_direction == "up":
        head[1] -= GRID_SIZE
    elif snake_direction == "down":
        head[1] += GRID_SIZE

    # Добавляем новый сегмент для головы змейки
    snake_segments.append(head)

    # Удаляем первый сегмент змейки
    snake_segments.pop(0)

# Функция для проверки столкновения змейки со стенами
def check_boundaries():
    head = snake_segments[-1]
    x = head[0]
    y = head[1]
    if x < 0 or x >= SCREEN_WIDTH:
        return True
    elif y < 0 or y >= SCREEN_HEIGHT:
        return True
    else:
        return False

# Функция для проверки столкновения змейки с едой
def check_food_collision(food_x, food_y):
    head = snake_segments[-1]
    if head[0] == food_x and head[1] == food_y:
        snake_segments.insert(0, [food_x, food_y])
        return True
    else:
        return False

# Создаем переменную для хранения направления движения змейки
snake_direction = "right"

# Создаем список для хранения сегментов змейки
snake_segments = [[0, 0], [GRID_SIZE, 0], [GRID_SIZE * 2, 0]]

# Создаем переменную для хранения координат еды
food_x = random.randint(0, SCREEN_WIDTH // GRID_SIZE - 1) * GRID_SIZE
food_y = random.randint(0, SCREEN_HEIGHT // GRID_SIZE - 1) * GRID_SIZE

# Создаем переменную для определения, нужно ли создать новую еду
spawn_food = False

# Создаем переменную для хранения счета
score = 0

# Запускаем игровой цикл
running = True
while running:
    # Обрабатываем события Pygame
   for event in pygame.event.get():
    if event.type == pygame.QUIT:
        running = False
    elif event.type == pygame.KEYDOWN:
        if event.key == pygame.K_RIGHT and snake_direction != "left":
            snake_direction = "right"
        elif event.key == pygame.K_LEFT and snake_direction != "right":
            snake_direction = "left"
        elif event.key == pygame.K_UP and snake_direction != "down":
            snake_direction = "up"
        elif event.key == pygame.K_DOWN and snake_direction != "up":
            snake_direction = "down"

# Очищаем экран
screen.fill(BLACK)

# Рисуем змейку
draw_snake()

# Двигаем змейку
move_snake()

# Проверяем столкновение со стенами
if check_boundaries():
    running = False

# Проверяем столкновение с едой
if check_food_collision(food_x, food_y):
    score += 1
    spawn_food = True

# Рисуем еду
pygame.draw.rect(screen, RED, (food_x, food_y, GRID_SIZE, GRID_SIZE))

# Если нужно создать новую еду, выбираем случайные координаты
# и проверяем, что они не пересекаются со змейкой
if spawn_food:
    while True:
        new_food_x = random.randint(0, SCREEN_WIDTH // GRID_SIZE - 1) * GRID_SIZE
        new_food_y = random.randint(0, SCREEN_HEIGHT // GRID_SIZE - 1) * GRID_SIZE
        for segment in snake_segments:
            if segment[0] == new_food_x and segment[1] == new_food_y:
                break
        else:
            break
    food_x = new_food_x
    food_y = new_food_y
    spawn_food = False

# Рисуем счет
font = pygame.font.SysFont(None, 30)
text = font.render("Счет: " + str(score), True, WHITE)
screen.blit(text, (10, 10))

# Обновляем экран
pygame.display.flip()
pygame.quit()
