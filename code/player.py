import pygame
from settings import PLAYER_MULTIPLIER
from support import import_folder

class Player(pygame.sprite.Sprite):
    def __init__(self,pos,groups,obstacle_sprites):
        super().__init__(groups)

        # image
        self.image = pygame.image.load('../graphics/player/down/down_1.png').convert_alpha()
        image_width = self.image.get_width()
        image_height = self.image.get_height()
        self.image = pygame.transform.scale(self.image,
            (image_width * PLAYER_MULTIPLIER, image_height * PLAYER_MULTIPLIER))
        self.rect = self.image.get_rect(topleft=(pos))
        self.hitbox = self.rect.inflate(0,-6)

        # movement
        self.direction = pygame.math.Vector2()
        self.speed = 4
        self.obstacle_sprites = obstacle_sprites

        self.import_player_assets()
        print(self.animations)

    def import_player_assets(self):
        path = '../graphics/player/'
        self.animations = {'up': [],'down': [],'left': [],'right': [],
                           'up_idle': [],'down_idle': [],'left_idle': [],'right_idle': [],
                           'up_attack': [],'down_attack': [],'left_attack': [],'right_attack': [],
                           'down_sleep': []
                           }
        for animation_key, animation_val in self.animations.items():
            self.animations[animation_key] = import_folder(f'{path}{animation_key}/')

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

        self.hitbox.y += self.direction.y * self.speed
        self.collision('vertical')
        self.hitbox.x += self.direction.x * self.speed
        self.collision('horizontal')
        self.rect.center = self.hitbox.center

    def collision(self,direction):
        if direction == 'vertical':
            for sprite in self.obstacle_sprites:
                if sprite.hitbox.colliderect(self.hitbox):
                    if self.direction.y > 0:  # moving down
                        self.hitbox.bottom = sprite.hitbox.top
                    if self.direction.y < 0:  # moving up
                        self.hitbox.top = sprite.hitbox.bottom
        if direction == 'horizontal':
            for sprite in self.obstacle_sprites:
                if sprite.hitbox.colliderect(self.hitbox):
                    if self.direction.x > 0:  # moving left
                        self.hitbox.right = sprite.hitbox.left
                    if self.direction.x < 0:  # moving right
                        self.hitbox.left = sprite.hitbox.right

    def update(self):
        self.input()
        self.move()
