import pygame
import sys
from config import WIDTH, HEIGHT, PLAYER_START_X, PLAYER_START_Y, FPS
from base import Player, Platform

pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Название Игры")

player = Player(PLAYER_START_X, PLAYER_START_Y)
platforms = [Platform(100, 500, 200, 20)]
platform = platforms[0] # Начальная платформа
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()

    player.move(keys)
    player.apply_gravity(1)
    player.check_platform_collision(platform)

    if keys[pygame.K_SPACE]:
        player.jump()

    # Зафиксированная камера
    camera_offset_x = WIDTH // 2 - player.rect.centerx
    camera_offset_y = HEIGHT // 2 - player.rect.centery

    screen.fill((0, 0, 0))

    # Отрисовка объектов с учетом смещения камеры
    screen.blit(
        player.image, (player.rect.x + camera_offset_x, player.rect.y + camera_offset_y)
    )
    screen.blit(
        platform.image,
        (platform.rect.x + camera_offset_x, platform.rect.y + camera_offset_y),
    )

    pygame.display.flip()

    clock.tick(FPS)
