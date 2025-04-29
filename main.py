import pygame
import sys


pygame.init()


WIDTH, HEIGHT = 800, 600
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Simple Platformer")


WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)

clock = pygame.time.Clock()

player_width, player_height = 50, 60
x, y = 100, HEIGHT - player_height - 50  
vel = 5
jumping = False
jump_speed = 10
gravity = 0.5
y_vel = 0

ground_y = HEIGHT - 50

running = True
while running:
    clock.tick(60)
    win.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        x -= vel
    if keys[pygame.K_RIGHT]:
        x += vel

    if not jumping:
        if keys[pygame.K_UP]:
            jumping = True
            y_vel = -jump_speed
    else:
        y_vel += gravity
        y += y_vel
        if y + player_height >= ground_y:
            y = ground_y - player_height
            jumping = False
            y_vel = 0

    pygame.draw.rect(win, GREEN, (0, ground_y, WIDTH, 50))

   
    pygame.draw.rect(win, BLUE, (x, y, player_width, player_height))

    pygame.display.update()


pygame.quit()
sys.exit()
