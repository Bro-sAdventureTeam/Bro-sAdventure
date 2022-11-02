import pygame
from settings import PLAYER_MULTIPLIER

class Player(pygame.sprite.Sprite):
    def __init__(self,pos,groups):
        super().__init__(groups)

        self.image = pygame.image.load('../graphics/player/down/down_1.png').convert_alpha()
        image_height = self.image.get_height()
        image_width = self.image.get_width()
        self.image = pygame.transform.scale(self.image,
                                            (image_width * PLAYER_MULTIPLIER, image_height * PLAYER_MULTIPLIER))
        self.rect = self.image.get_rect(topleft=(pos))