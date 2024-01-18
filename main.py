import pygame
import sys

from base import Player, Platform
from config.window import WIDTH, HEIGHT


class Game:
    def __init__(self):
        self.player = Player(200, 50)
        self.platforms = [
            Platform(200, 400, 150, 20),
            Platform(200, 500, 150, 20),
            Platform(400, 300, 150, 20),
            Platform(400, 100, 150, 20),
        ]

    def update(self):
        self.player.update(self.platforms)

    def draw(self):
        screen.fill((255, 255, 255))

        for platform in self.platforms:
            platform.draw(screen)

        self.player.draw(screen)

        pygame.display.flip()


if __name__ == "__main__":
    pygame.init()

    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Simple Platformer")
    clock = pygame.time.Clock()

    game = Game()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        game.update()
        game.draw()
        clock.tick(60)
