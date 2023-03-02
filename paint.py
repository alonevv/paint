import pygame

WIDTH = 480
HEIGHT = 600
FPS = 120
prs = False

# Задаем цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
PURPLE = (188 ,25, 255)
colors = {1: WHITE, 2: BLACK, 3: RED, 4: GREEN, 5: BLUE, 6: YELLOW, 7: PURPLE}

# Создаем игру и окно
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Игра")
clock = pygame.time.Clock()
#background_image = pygame.image.load('gun.jpg')


class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50, 40))
        self.image.fill(PURPLE)
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH / 2
        self.rect.bottom = HEIGHT - 10
        self.speedx = 0
        self.speedy = 0

    def update(self):

        mousepos = pygame.mouse.get_pos()
        self.rect.x = mousepos[0]
        self.rect.y = mousepos[1]
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_1]:
            self.image.fill(colors[1])
        if keystate[pygame.K_2]:
            self.image.fill(colors[2])
        if keystate[pygame.K_3]:
            self.image.fill(colors[3])
        if keystate[pygame.K_4]:
            self.image.fill(colors[4])
        if keystate[pygame.K_5]:
            self.image.fill(colors[5])
        if keystate[pygame.K_6]:
            self.image.fill(colors[6])
        if keystate[pygame.K_7]:
            self.image.fill(colors[7])

all_sprites = pygame.sprite.Group()
player = Player()
all_sprites.add(player)
# Цикл игры
running = True
while running:
    # Держим цикл на правильной скорости
    clock.tick(FPS)
    # Ввод процесса (события)
    for event in pygame.event.get():
        # проверка для закрытия окна
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            prs = True
        if event.type == pygame.MOUSEBUTTONUP:
            prs = False

    # Обновление
    all_sprites.update()
    # Рендеринг
    #screen.fill(BLUE)
    if prs==True:
        all_sprites.draw(screen)
    # После отрисовки всего, переворачиваем экран
    pygame.display.flip()

pygame.quit()
