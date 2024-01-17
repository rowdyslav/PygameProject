import pygame
from pygame.rect import Rect
from pygame.surface import Surface

from config.player import SPEED, JUMP_SPEED


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

        self.status: str = 'idle'
        self.on_ground = False
        self.direction = pygame.math.Vector2(0, 0)
        self.facing_right: bool | None = None
        self.gravity = 1

        self.image = pygame.image.load("sprites/player.png")
        self.rect: Rect = self.image.get_rect()
        self.rect.topleft = (x, y)

        self.speed: int = SPEED
        self.jump_speed: int = JUMP_SPEED

        self.hitbox = pygame.Rect(self.rect.topleft, (50, self.rect.height))

    def get_input(self) -> None:
        """
        Обрабатывает кнопки
        """
        keys = pygame.key.get_pressed()

        if keys[pygame.K_RIGHT]:
            self.direction.x = 1
            self.facing_right = True
        elif keys[pygame.K_LEFT]:
            self.direction.x = -1
            self.facing_right = False
        else:
            self.direction.x = 0

        if keys[pygame.K_SPACE] and self.on_ground:
            self.jump()

    def apply_gravity(self) -> None:
        """
        Применяет гравитацию к вертикальной скорости игрока.
        """
        self.direction.y += self.gravity
        self.hitbox.y += self.direction.y

    def check_platform_collision(self, platform: Platform) -> None:
        """
        Проверяет столкновение игрока с платформой и обрабатывает его.

        :param platform: Объект платформы для проверки столкновения.
        """
        if self.rect.colliderect(platform.rect) and self.jump_speed > 0:
            self.jump_speed = 0
            self.rect.y = platform.rect.y - self.rect.height
            self.on_ground = True

    def jump(self) -> None:
        """
        Выполняет прыжок, если игрок не находится в процессе прыжка.
        """
        if self.on_ground:
            self.direction.y = self.jump_speed

    def get_status(self):
        if self.direction.y < 0:
            self.status = "jump"
        elif self.direction.y > 1:
            self.status = "fall"
        else:
            if self.direction.x != 0:
                self.status = "run"
            else:
                self.status = "idle"

    def update(self, *args, **kwargs):
        self.get_input()
        self.get_status()


