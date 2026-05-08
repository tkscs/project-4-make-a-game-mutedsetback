import pygame
import random

pygame.init()
 
WIDTH, HEIGHT = 400, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Game")
clock = pygame.time.Clock()
 
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
player = pygame.Rect(180, 520, 40, 40)
enemy = pygame.Rect(random.randint(0, WIDTH - 40), 0, 40, 40)
 
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player.left > 0:
        player.x -= 5
    if keys[pygame.K_RIGHT] and player.right < WIDTH:
        player.x += 5
    enemy.y += 5
    if enemy.top > HEIGHT:
        enemy.x = random.randint(0, WIDTH - 40)
        enemy.y = 0
    screen.fill(WHITE)
    pygame.draw.rect(screen, BLUE, player)
    pygame.draw.rect(screen, RED, enemy)
    pygame.display.update()
    clock.tick(60)
 
pygame.quit()