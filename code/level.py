import pygame
from settings import TILESIZE
from support import import_csv_layout
from player import Player
from tile import Tile
from ui import UI

class Level:
    def __init__(self):

        # get the display surface
        self.display_surf = pygame.display.get_surface()

        # sprite group setup
        self.visible_sprites = YSortCameraGroup()
        self.obstacle_sprites = pygame.sprite.Group()

        # create map
        self.create_map()

        self.ui = UI()

    def create_map(self):
        layouts = {
            'boundary': import_csv_layout('../map/map_FloorBlocks.csv'),
            'floor': import_csv_layout('../map/map_Floor.csv'),
            'objects': import_csv_layout('../map/map_Objects.csv'),
            'entities': import_csv_layout('../map/map_Entities.csv')
        }

        objects = {
            'box_big': pygame.image.load('../graphics/obstacle/01.png').convert_alpha(),
            'box_small': pygame.image.load('../graphics/obstacle/02.png').convert_alpha(),
            'barrel': pygame.image.load('../graphics/obstacle/03.png').convert_alpha(),
            'torch': pygame.image.load('../graphics/obstacle/04.png').convert_alpha()
        }

        for layout_key, layout_value in layouts.items():
            for row_index, row in enumerate(layout_value):
                for col_index, col in enumerate(row):
                    x = col_index * TILESIZE
                    y = row_index * TILESIZE
                    if layout_key == 'boundary':
                        if col == '0':
                            Tile((x,y),[self.obstacle_sprites])

                    if layout_key == 'objects':
                        if col == '2713':
                            Tile((x,y),
                                 [self.obstacle_sprites, self.visible_sprites],
                                 objects['box_small'])
                        elif col == '2432':
                            Tile((x,y),
                                 [self.obstacle_sprites,self.visible_sprites],
                                 objects['box_big'])
                        elif col == '2533':
                            Tile((x,y),
                                 [self.obstacle_sprites,self.visible_sprites],
                                 objects['barrel'])
                        elif col == '2992':
                            Tile((x,y),
                                 [self.obstacle_sprites,self.visible_sprites],
                                 objects['torch'])

                    elif layout_key == 'entities':
                        if col == '3721':
                            self.player = Player((x,y),
                                                 [self.visible_sprites],
                                                 self.obstacle_sprites)

    def run(self):
        self.visible_sprites.custom_draw(self.player)
        self.visible_sprites.update()
        self.ui.display(self.player)


class YSortCameraGroup(pygame.sprite.Group):
    def __init__(self):

        # general setup
        super().__init__()
        self.display_surface = pygame.display.get_surface()
        self.half_width = self.display_surface.get_width() // 2
        self.half_height = self.display_surface.get_height() // 2
        self.offset = pygame.math.Vector2()

        # creating the floor
        self.floor_surf = pygame.image.load('../graphics/tilemap/ground.png').convert()
        self.floor_rect = self.floor_surf.get_rect(topleft = (0,0))

    def custom_draw(self,player):

        # getting the offset
        self.offset.x = player.rect.centerx - self.half_width
        self.offset.y = player.rect.centery - self.half_height

        # drawing the floor
        floor_offset_pos = self.floor_rect.topleft - self.offset
        self.display_surface.blit(self.floor_surf,floor_offset_pos)

        # drawing the sprites
        # for sprite in self.sprites():
        for sprite in sorted(self.sprites(),key = lambda sprite: sprite.rect.centery):
            offset_rect = sprite.rect.topleft - self.offset
            self.display_surface.blit(sprite.image,offset_rect)
