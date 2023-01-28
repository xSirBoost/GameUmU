import pygame
from settings import *
from tile import Tile
from player import Player
from debug import debug
from support import *
from random import choice
from weapon import Weapon
from ui import ui
from enemy import Enemy

class Level:
    def __init__(self):
        self.display_surface = pygame.display.get_surface()
        self.visible_sprites = YSortCameraGroup()
        self.obstacles_sprites = pygame.sprite.Group()
        self.current_attack = None
        self.attack_sprites = pygame.sprite.Group()
        self.attackable_sprites = pygame.sprite.Group()

        self.create_map()
        self.ui = ui()

    def create_map(self):

        layout = {
            'boundary' : import_csv_layout('./graphics/map/map_FloorBlocks.csv'),
            'grass' : import_csv_layout('./graphics/map/map_Grass.csv'),
            'object' : import_csv_layout('./graphics/map/map_Objects.csv'),
            'entities' : import_csv_layout('./graphics/map/map_entities.csv')
        }
        graphics = {
            'grass' : import_folder('./graphics/Grass'),
            'objects' : import_folder('./graphic/objects'),
        }

        for style,layout in layout.items():
            for row_index, row in enumerate(layout):
                for col_index, col in enumerate(row):
                    if col != '-1':
                        x = col_index * TILESIZE
                        y = row_index * TILESIZE
                        if style == 'boundary' :
                            Tile((x,y),[self.obstacles_sprites], 'invisible')
                        if style == 'grass' :
                            random_grass_image = choice(graphics['grass'])
                            Tile((x,y),[self.visible_sprites,self.obstacles_sprites,self.attackable_sprites],'grass',random_grass_image)
                        if style == 'object' : 
                            pass
                        if style == 'entities':
                            if col == '394':
                                self.player = Player((x,y),[self.visible_sprites], self.obstacles_sprites,self.create_attack, self.destroy_weapon, self.create_magic)
                            else:
                                print(col)
                                if col == '391': monster_name = 'bamboo'
                                elif col == '391': monster_name = 'spirit'
                                elif col == '392': monster_name = 'raccoon'
                                else: 
                                    monster_name = 'squid'
                                Enemy(monster_name,(x,y),[self.visible_sprites,self.attackable_sprites],self.obstacles_sprites)

    def create_attack(self):
        self.current_attack = Weapon(self.player,[self.visible_sprites,self.attack_sprites])

    def create_magic(self,style,strength,cost):
        print('strength')
        print('cost')

    def destroy_weapon(self):
        if self.current_attack:
            self.current_attack.kill()
        self.current_attack = None

    def player_attack_logic(self):
        if self.attack_sprites:
            for attack_sprite in self.attack_sprites:
                collision_sprites = pygame.sprite.spritecollide(attack_sprite,self.attackable_sprites,False)
                if collision_sprites:
                    for target_sprite in collision_sprites:
                        if target_sprite.sprite_type == 'grass':
                            target_sprite.kill()
                        else:
                            target_sprite.get_damage(self.player,attack_sprite.sprite_type)

    def run(self):
        
        self.visible_sprites.custom_draw(self.player)
        self.visible_sprites.update()
        self.visible_sprites.enemy_update(self.player)
        self.player_attack_logic()
        self.ui.display(self.player)

        

class YSortCameraGroup(pygame.sprite.Group):
    def __init__(self):
        super().__init__()

        self.display_surface = pygame.display.get_surface()
        self.half_width = self.display_surface.get_size()[0] // 2
        self.half_height = self.display_surface.get_size()[1] // 2
        self.offset = pygame.math.Vector2()

        self.floor_surf = pygame.image.load('./graphics/tilemap/ground.png')
        self.floor_rect = self.floor_surf.get_rect(topleft = (0,0))


    def custom_draw(self,player):
        self.offset.x = player.rect.centerx - self.half_width
        self.offset.y = player.rect.centery - self.half_height

        floor_offset_pos = self.floor_rect.topleft - self.offset
        self.display_surface.blit(self.floor_surf,floor_offset_pos)
        
        for sprite in sorted(self.sprites(),key = lambda sprite:sprite.rect.centery):

            offset_pos = sprite.rect.topleft - self.offset
            self.display_surface.blit(sprite.image,offset_pos)

    def enemy_update(self,player):
        enemy_sprites = [sprite for sprite in self.sprites() if hasattr(sprite,'sprite_type') and sprite.sprite_type == 'enemy']
        for enemy in enemy_sprites:
            enemy.enemy_update(player)