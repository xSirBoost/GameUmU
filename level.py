import pygame
from settings import *
from tile import Tile
from player import Player
from debug import debug
from support import *
from random import choice
from weapon import Weapon
from ui import ui

class Level:
    def __init__(self):

        self.display_surface = pygame.display.get_surface()
        
        self.visible_sprites = YSortCameraGroup()
        self.obstacles_sprites = pygame.sprite.Group()

        self.current_attack = None


        self.create_map()

        self.ui = ui()

    def create_map(self):

        layout = {
            'boundary' : import_csv_layout('./graphics/map/map_FloorBlocks.csv'),
            'grass' : import_csv_layout('./graphics/map/map_Grass.csv'),
            'object' : import_csv_layout('./graphics/map/map_Objects.csv'),
        }
        graphics = {
            'grass' : import_folder('./graphics/Grass'),
            'objects' : import_folder('./graphic/objects'),
        }

        for style,layout in layout.items():
            for row_index, row in enumerate(layout):
                for col_index, col in enumerate(row):
                    if col != '-1':
                        print(col)
                        x = col_index * TILESIZE
                        y = row_index * TILESIZE
                        if style == 'boundary' :
                            Tile((x,y),[self.obstacles_sprites], 'invisible')
                        if style == 'grass' :
                            random_grass_image = choice(graphics['grass'])
                            Tile((x,y),[self.visible_sprites,self.obstacles_sprites],'grass',random_grass_image)
                        if style == 'object' : 
                            pass
                            #surf = graphics['objects'][int(col)]
                            #Tile((x,y),[self.visible_sprites,self.obstacle_sprites],'object',surf)


        self.player = Player((2000,1430),[self.visible_sprites], self.obstacles_sprites,self.create_attack, self.destroy_weapon)

    def create_attack(self):
        self.current_attack = Weapon(self.player,[self.visible_sprites])

    def destroy_weapon(self):
        if self.current_attack:
            self.current_attack.kill()
        self.current_attack = None

    def run(self):
        
        self.visible_sprites.custom_draw(self.player)
        self.visible_sprites.update()
        self.ui.display(self.player)
        

class YSortCameraGroup(pygame.sprite.Group):
    def __init__(self):
        #general setup
        super().__init__()

        self.display_surface = pygame.display.get_surface()
        self.half_width = self.display_surface.get_size()[0] // 2
        self.half_height = self.display_surface.get_size()[1] // 2
        self.offset = pygame.math.Vector2()

        #creating the floor
        self.floor_surf = pygame.image.load('./graphics/tilemap/ground.png')
        self.floor_rect = self.floor_surf.get_rect(topleft = (0,0))


    def custom_draw(self,player):

        # getting offset
        self.offset.x = player.rect.centerx - self.half_width
        self.offset.y = player.rect.centery - self.half_height

        floor_offset_pos = self.floor_rect.topleft - self.offset
        self.display_surface.blit(self.floor_surf,floor_offset_pos)
        
        #for sprite in self.sprites():
        for sprite in sorted(self.sprites(),key = lambda sprite:sprite.rect.centery):

            offset_pos = sprite.rect.topleft - self.offset
            self.display_surface.blit(sprite.image,offset_pos)

        