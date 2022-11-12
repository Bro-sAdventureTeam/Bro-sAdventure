import pygame

class UI:
    def __init__(self):
        self.display_surf = pygame.display.get_surface()

    def inventory_blocks(self,pos):
        self.image = pygame.image.load('../graphics/ui/inventory_block.png').convert_alpha()
        self.image_scaled = pygame.transform.scale(self.image,
            ((self.image.get_height() * 2),(self.image.get_width() * 2)))
        self.rect = self.image.get_rect(topleft = (pos))

        self.display_surf.blit(self.image_scaled,self.rect)

    def display(self,player):
        for i in range(6):
            self.inventory_blocks((539+(i*34),670))
