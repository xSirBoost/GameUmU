import pygame 
from settings import *

class ui:
    def __init__(self):
        self.display_surface = pygame.display.get_surface()
        self.font = pygame.font.Font(ui_font,ui_font_size)

        self.health_bar_rect = pygame.Rect(10, 10, health_bar_width, bar_height)
        self.energy_bar_rect = pygame.Rect(10, 34, energy_bar_width, bar_height)

        self.weapon_graphics = []
        for weapon in weapon_data.values():
            path = weapon['graphics']
            weapon = pygame.image.load(path).convert_alpha()
            self.weapon_graphics.append(weapon)

        self.magic_graphics = []
        for magic in magic_data.values():
            magic = pygame.image.load(magic['graphics']).convert_alpha()
            self.magic_graphics.append(magic)


    def show_bar(self, current, max_amount, bg_rect, colour):
        pygame.draw.rect(self.display_surface, ui_bg_colour, bg_rect)

        ratio = current / max_amount
        current_width = bg_rect.width * ratio
        current_rect = bg_rect.copy()
        current_rect.width = current_width

        pygame.draw.rect(self.display_surface,colour,current_rect)
        pygame.draw.rect(self.display_surface,ui_border_colour,bg_rect,3)

    def show_exp(self,exp):
        text_surf = self.font.render(str(int(exp)), False, text_color)
        x = self.display_surface.get_size()[0] - 20
        y = self.display_surface.get_size()[1] - 20
        text_rect = text_surf.get_rect(bottomright = (x, y ))
        pygame.draw.rect(self.display_surface, ui_bg_colour, text_rect.inflate(20,20))
        self.display_surface.blit(text_surf, text_rect)

    def weapon_box(self, left, top):
        bg_rect = pygame.Rect(left, top, item_box_size, item_box_size)
        pygame.draw.rect(self.display_surface,ui_bg_colour,bg_rect)
        pygame.draw.rect(self.display_surface,ui_border_colour,bg_rect, 3)
        return bg_rect

    def weapon_overlay(self,weapon_index):
        bg_rect = self.weapon_box(10,630)
        weapon_surf = self.weapon_graphics[weapon_index]
        weapon_rect = weapon_surf.get_rect(center = bg_rect.center)
        self.display_surface.blit(weapon_surf,weapon_rect)

    def magic_overlay(self,magic_index):
        bg_rect = self.weapon_box(90,630)
        magic_surf = self.magic_graphics[magic_index]
        magic_rect = magic_surf.get_rect(center = bg_rect.center)
        self.display_surface.blit(magic_surf,magic_rect)

    def display(self, player):
        self.show_bar(player.health,player.stats['health'], self.health_bar_rect, health_colour)
        self.show_bar(player.energy,player.stats['energy'], self.energy_bar_rect, energy_colour)

        self.show_exp(player.exp)

        self.weapon_overlay(player.weapon_index)
        self.magic_overlay(player.magic_index)