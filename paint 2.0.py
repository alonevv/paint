import pygame

WIDTH = 1920
HEIGHT = 1080
FPS = 120
prs = False

#Задаем цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
PURPLE = (188, 25, 255)
colors = {1: WHITE, 2: BLACK, 3: RED, 4: GREEN, 5: BLUE, 6: YELLOW, 7: PURPLE}
color = colors[7]
size = 30

# Создаем игру и окно
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Игра")
clock = pygame.time.Clock()

#Цикл игры
running = True
while running:

    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            prs = True
        if event.type == pygame.MOUSEBUTTONUP:
            prs = False

    keystate = pygame.key.get_pressed()
    if keystate[pygame.K_1]:
        color = colors[1]
    if keystate[pygame.K_2]:
        color = colors[2]
    if keystate[pygame.K_3]:
        color = colors[3]
    if keystate[pygame.K_4]:
        color = colors[4]
    if keystate[pygame.K_5]:
        color = colors[5]
    if keystate[pygame.K_6]:
        color = colors[6]
    if keystate[pygame.K_7]:
        color = colors[7]

    if keystate[pygame.K_h]:
        size += 1
    if keystate[pygame.K_j] and size > 3:
        size -= 1

    if prs == True:
        pygame.draw.circle(screen, color, pygame.mouse.get_pos(), size)

    pygame.display.flip()

pygame.quit()
