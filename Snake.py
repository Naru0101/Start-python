#Проект № 5 )+
import pygame
import random

pygame.init()

BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
WHITE = (255, 255, 255)

screen_width = 1280
screen_height = 720
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Snake")

cell_size = 20
snake_speed = 10
x_change = 0
y_change = 0
x = screen_width // 2
y = screen_height // 2
snake_body = []
snake_length = 1

food_x = round(random.randrange(0, screen_width - cell_size) / cell_size) * cell_size
food_y = round(random.randrange(0, screen_height - cell_size) / cell_size) * cell_size

score = 0
deaths = 0

font = pygame.font.Font(None, 36)

def draw_snake(snake_body):
    for block in snake_body:
        pygame.draw.rect(screen, GREEN, [block[0], block[1], cell_size, cell_size])

def draw_food(food_x, food_y):
    pygame.draw.rect(screen, RED, [food_x, food_y, cell_size, cell_size])

def update_screen():
    screen.fill(BLACK)
    draw_snake(snake_body)
    draw_food(food_x, food_y)

    score_text = font.render("Score: " + str(score), True, WHITE)
    deaths_text = font.render("Deaths: " + str(deaths), True, WHITE)
    screen.blit(score_text, (10, 10))
    screen.blit(deaths_text, (10, 50))

    pygame.display.update()

running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x_change = -cell_size
                y_change = 0
            elif event.key == pygame.K_RIGHT:
                x_change = cell_size
                y_change = 0
            elif event.key == pygame.K_UP:
                x_change = 0
                y_change = -cell_size
            elif event.key == pygame.K_DOWN:
                x_change = 0
                y_change = cell_size

    x += x_change
    y += y_change

    if x >= screen_width or x < 0 or y >= screen_height or y < 0:
        deaths += 1
        x = screen_width // 2
        y = screen_height // 2
        snake_body = []
        snake_length = 1

    if x == food_x and y == food_y:
        score += 1
        food_x = round(random.randrange(0, screen_width - cell_size) / cell_size) * cell_size
        food_y = round(random.randrange(0, screen_height - cell_size) / cell_size) * cell_size
        snake_length += 1

    snake_head = []
    snake_head.append(x)
    snake_head.append(y)
    snake_body.append(snake_head)

    if len(snake_body) > snake_length:
        del snake_body[0]

    update_screen()
    clock.tick(snake_speed)

pygame.quit()