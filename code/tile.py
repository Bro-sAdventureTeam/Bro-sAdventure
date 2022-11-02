import pygame
from settings import TILESIZE, PLAYER_MULTIPLIER

class Tile(pygame.sprite.Sprite):
    def __init__(self,pos,groups):
        super().__init__(groups)

        self.image = pygame.image.load('../draft/graphics/obstacle/coin.png')
        self.image = pygame.transform.scale(self.image,
                                            (TILESIZE,TILESIZE))
        self.rect = self.image.get_rect(topleft = pos)
