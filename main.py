import pygame
import sys

from base import Player, Platform

from config.window import WIDTH, HEIGHT, FPS
from config.player import START_X, START_Y

pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Название Игры")

player = Player(START_X, START_Y)
platforms = [Platform(100, 500, 200, 20)]
start_platform = platforms[0]
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill('grey')

    pygame.display.update()
    clock.tick(FPS)
