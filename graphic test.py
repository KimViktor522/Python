import pygame

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (125, 125, 125)
LIGHT_BLUE = (64, 128, 255)
GREEN = (0, 200, 64)
YELLOW = (225, 225, 0)
PINK = (230, 50, 230)

FPS = 60
max_width = 1080 # ширина x
max_height = 2340 # высота y

#координаты и размеры 
x = 0
y = 1000
r = 50

pygame.init()
 
sc = pygame.display.set_mode((0, 0))
clock = pygame.time.Clock()
# здесь будут рисоваться фигуры
pygame.draw.line(sc, WHITE, [10, 500], [1000, 35])
pygame.draw.circle(sc, YELLOW, (100, 100), 100)
pygame.display.update()
# конец

while 1:
    sc.fill(BLACK)
    for i in pygame.event.get():
        if i.type == pygame.QUIT: exit()

    pygame.draw.circle(sc, PINK, (x, y), r)
    pygame.display.update()
    if (x >= max_width + r):
        x = r
    else:
        x+=5
    clock.tick(FPS)
