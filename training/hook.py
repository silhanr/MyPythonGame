import pygame
from pygame.rect import Rect
from training.character import MainCharacter

INCREMENT = 20

class Hook(Rect):


    def center_hook(self, game_character):

        self.midbottom = (game_character.position_x + game_character.image_size[0] / 2,
                          game_character.position_y)

    def shot(self, game_character):
        """
        self.top = self.top - INCREMENT

        self.bottom = game_character.position_y
        """
        print('shot')
        self.inflate_ip(0,INCREMENT)
        self.bottom = game_character.position_y













