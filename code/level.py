import pygame
from settings import TILESIZE
from support import import_csv_layout
from player import Player

class Level:
    def __init__(self):

        # get the display surface
        self.display_surf = pygame.display.get_surface()

        # sprite group setup
        self.visible_sprites = pygame.sprite.Group()
        self.obstacle_sprites = pygame.sprite.Group()

        # create map
        self.create_map()

    def create_map(self):
        layouts = {
            'entities': import_csv_layout('../draft/map/map_Entities.csv'),
            'floor': import_csv_layout('../draft/map/map_Floor.csv'),
            'boundary': import_csv_layout('../draft/map/map_FloorBlocks.csv'),
            'objects': import_csv_layout('../draft/map/map_Objects.csv')
        }
        for layout in layouts.values():
            for row_index, row in enumerate(layout):
                for col_index, col in enumerate(row):
                    x = col_index * TILESIZE
                    y = row_index * TILESIZE
                    if col == '3721':
                        Player((x,y),[self.visible_sprites])


    def run(self):
        self.visible_sprites.draw(self.display_surf)
        