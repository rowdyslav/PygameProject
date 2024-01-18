import pygame

from config.window import HEIGHT


class Platform:
    def __init__(self, x, y, width, height):
        self.rect = pygame.Rect(x, y, width, height)

    def draw(self, screen):
        pygame.draw.rect(screen, (0, 255, 0), self.rect)


class Player:
    def __init__(self, x, y):
        self.image = pygame.image.load('sprites/graphics/player.png')
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = self.start_position = x, y
        self.velocity = 0
        self.gravity = 1
        self.jump_power = -15
        self.on_ground = False

    def update(self, platforms):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rect.x -= 5
        if keys[pygame.K_d]:
            self.rect.x += 5

        self.apply_gravity()

        if keys[pygame.K_SPACE] and self.on_ground:
            self.jump()

        self.check_collision(platforms)
        self.check_alive()

    def apply_gravity(self):
        if not self.on_ground:
            self.velocity += self.gravity
        else:
            self.velocity = 0

        self.rect.y += self.velocity

    def jump(self):
        self.velocity = self.jump_power

    def check_collision(self, platforms):
        self.on_ground = False

        for platform in platforms:
            if self.rect.colliderect(platform.rect):
                self.rect.y = platform.rect.y - self.rect.height
                self.on_ground = True
                break

    def check_alive(self):
        if self.rect.y > HEIGHT:
            self.rect.x, self.rect.y = self.start_position

        ...  # TODO: сюда все проверки определяющие жив ли игрок

    def draw(self, screen):
        screen.blit(self.image, self.rect)
