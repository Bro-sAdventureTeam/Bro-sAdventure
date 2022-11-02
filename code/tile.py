import pygame

class Tile(pygame.sprite.Sprite):
    def __init__(self,pos,groups):
        super().__init__(groups)

        self.image = pygame.image.load('../draft/graphics/obstacle/coin.png')
        self.rect = self.image.get_rect(topleft = pos)