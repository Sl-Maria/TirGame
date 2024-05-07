import pygame
import random

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Тир")
icon = pygame.image.load("img/icons.png")
pygame.display.set_icon(icon)

target_image = pygame.image.load("img/target.png")
target_width = 58
target_height = 50
target_x = random.randint(0, SCREEN_WIDTH - target_width)
target_y = random.randint(0, SCREEN_HEIGHT - target_height)
target_speed_x = random.choice([-1, 1])  # Уменьшенная скорость
target_speed_y = random.choice([-1, 1])  # Уменьшенная скорость

color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

score = 0
font = pygame.font.Font(None, 36)
fail_score = 0

clock = pygame.time.Clock()  # Создание объекта Clock для контроля кадров
clock_speed = 30             # Скорость кадров

running = True
while running:
    screen.fill(color)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if target_x < mouse_x < target_x + target_width and target_y < mouse_y < target_y + target_height:
                score += 1
                clock_speed += 5
                target_x = random.randint(0, SCREEN_WIDTH - target_width)
                target_y = random.randint(0, SCREEN_HEIGHT - target_height)
                target_speed_x = random.choice([-1, 1])
                target_speed_y = random.choice([-1, 1])
            else:
                fail_score += 1

    target_x += target_speed_x
    target_y += target_speed_y

    if target_x < 0 or target_x > SCREEN_WIDTH - target_width:
        target_speed_x = -target_speed_x
    if target_y < 0 or target_y > SCREEN_HEIGHT - target_height:
        target_speed_y = -target_speed_y

    screen.blit(target_image, (target_x, target_y))
    score_text = font.render(f"Попадания: {score}", True, (255, 255, 255))
    screen.blit(score_text, (10, 10))
    fail_score_text = font.render(f"Промахи: {fail_score}", True, (255, 255, 255))
    screen.blit(fail_score_text, (10, 35))

    pygame.display.update()
    clock.tick(clock_speed)  # Ограничение до 60 кадров в секунду

pygame.quit()