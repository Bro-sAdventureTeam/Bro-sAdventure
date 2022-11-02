import pygame
from settings import PLAYER_MULTIPLIER

class Player(pygame.sprite.Sprite):
    def __init__(self,pos,groups):
        super().__init__(groups)

        # image
        self.image = pygame.image.load('../graphics/player/down/down_1.png').convert_alpha()
        image_height = self.image.get_height()
        image_width = self.image.get_width()
        self.image = pygame.transform.scale(self.image,
            (image_width * PLAYER_MULTIPLIER, image_height * PLAYER_MULTIPLIER))
        self.rect = self.image.get_rect(topleft=(pos))

        # movement
        self.direction = pygame.math.Vector2()
        self.speed = 2

    def input(self):
        keys = pygame.key.get_pressed()

        # movement input
        if keys[pygame.K_w]:
            self.direction.y = -1
        elif keys[pygame.K_s]:
            self.direction.y = 1
        else:
            self.direction.y = 0

        if keys[pygame.K_a]:
            self.direction.x = -1
        elif keys[pygame.K_d]:
            self.direction.x = 1
        else:
            self.direction.x = 0

    def move(self):
        if self.direction.magnitude() != 0:
            self.direction = self.direction.normalize()
        self.rect.y += self.direction.y * self.speed
        self.rect.x += self.direction.x * self.speed

    def update(self):
        self.input()
        self.move()
