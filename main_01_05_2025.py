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
jump_speed = 12  # 🔼 Higher jump
gravity = 0.5
y_vel = 0

ground_y = HEIGHT - 50
platform = pygame.Rect(300, 450, 200, 20)  # 🔽 Lower platform so it's reachable


running = True
on_ground_or_platform = False  # Track if standing

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

    player_rect = pygame.Rect(x, y, player_width, player_height)

    # Apply jump
    if keys[pygame.K_UP] and on_ground_or_platform:
        y_vel = -jump_speed

    # Gravity always applies
    y_vel += gravity
    y += y_vel
    player_rect.y = y  # Update after moving

    # Reset standing flag
    on_ground_or_platform = False

    # Ground collision
    if y + player_height >= ground_y:
        y = ground_y - player_height
        y_vel = 0
        on_ground_or_platform = True

    # Platform collision from top
    if player_rect.colliderect(platform) and y_vel > 0:
        if player_rect.bottom - platform.top < 15:
            y = platform.top - player_height
            y_vel = 0
            on_ground_or_platform = True

    # Draw ground and platform
    pygame.draw.rect(win, GREEN, (0, ground_y, WIDTH, 50))       # Ground
    pygame.draw.rect(win, GREEN, platform)                       # Platform
    pygame.draw.rect(win, BLUE, (x, y, player_width, player_height))  # Player

    pygame.display.update()

pygame.quit()
sys.exit()
