import pygame
from pygame.rect import Rect
from pygame.surface import Surface
from pygame.key import ScancodeWrapper

from config import PLAYER_SPEED, PLAYER_JUMP_POWER


class Platform(pygame.sprite.Sprite):
    def __init__(self, x: int, y: int, width: int, height: int):
        """
        :param x: Координата X начальной позиции платформы.
        :param y: Координата Y начальной позиции платформы.
        :param width: Ширина платформы.
        :param height: Высота платформы.
        """
        super().__init__()
        self.image: Surface = pygame.Surface((width, height))
        self.image.fill((255, 255, 255))
        self.rect: Rect = self.image.get_rect()
        self.rect.topleft = (x, y)


class Player(pygame.sprite.Sprite):
    def __init__(self, x: int, y: int):
        """
        :param x: Координата X начальной позиции игрока.
        :param y: Координата Y начальной позиции игрока.
        """
        super().__init__()
        self.image = pygame.image.load("sprites/player.png")
        self.rect: Rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.speed: int = PLAYER_SPEED
        self.y_speed: int = 0
        self.is_jumping: bool = False

    def move(self, keys: ScancodeWrapper) -> None:
        """
        Обрабатывает движение игрока влево и вправо.

        :param keys: Список кодов клавиш, представляющих текущее состояние клавиш.
        """
        if keys[pygame.K_a]:
            self.rect.x -= self.speed
        if keys[pygame.K_d]:
            self.rect.x += self.speed

    def apply_gravity(self, gravity: int) -> None:
        """
        Применяет гравитацию к вертикальной скорости игрока.

        :param gravity: Значение гравитации, влияющей на скорость игрока.
        """
        self.y_speed += gravity
        self.rect.y += self.y_speed

    def check_platform_collision(self, platform: Platform) -> None:
        """
        Проверяет столкновение игрока с платформой и обрабатывает его.

        :param platform: Объект платформы для проверки столкновения.
        """
        if self.rect.colliderect(platform.rect) and self.y_speed > 0:
            self.y_speed = 0
            self.rect.y = platform.rect.y - self.rect.height
            self.is_jumping = False

    def jump(self) -> None:
        """
        Выполняет прыжок, если игрок не находится в процессе прыжка.
        """
        if not self.is_jumping:
            self.y_speed = PLAYER_JUMP_POWER
            self.is_jumping = True
