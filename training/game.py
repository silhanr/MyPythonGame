# import pygame module
import time

import pygame, os, configparser

from training.character import MainCharacter


class SimpleGame:
    def __init__(self):
        self.root_path = "../../MyPythonGame"

        self.main_screen = None
        self.resolution = [1000, 500]
        self.main_character = MainCharacter()




        # initialize the pygame module
        pygame.init()

    def main(self):

        self.open_window(self.resolution[0], self.resolution[1])
        step_x = 10
        step_y = 10

        running = True

        # main loop
        while running:
            # event handling, gets all event from the event queue
            for event in pygame.event.get():
                # only do something if the event is of type QUIT
                if event.type == pygame.QUIT:
                    # change the value to False, to exit the main loop
                    running = False
            if self.main_character.position_x > \
                self.resolution[0]-self.main_character.image_size[0] \
                    or self.main_character.position_x < 0:
                step_x = -step_x
            if self.main_character.position_y > \
                    self.resolution[1] - self.main_character.image_size[1] \
                    or self.main_character.position_y < 0:
                step_y = -step_y
            self.main_character.position_x += step_x
            self.main_character.position_y += step_y

            self.main_screen.blit(self.main_character.character_image,
                                  (self.main_character.position_x, \
                                   self.main_character.position_y))
            #time.sleep(1)
            pygame.display.flip()







    def open_window(self,width, height):
        """
        This method creates a gaming window
        :param height:
        :param width:
        :return:
        """
        self.main_screen = pygame.display.set_mode((width,height))

        #background
        self.main_screen.blit(
            pygame.image.load(
                os.path.join(self.root_path, "images", "background.jpg")), (0,0))

        pos_x = self.main_character.position_x
        pos_y = self.main_character.position_y

        self.main_screen.blit(self.main_character.character_image,
                              (pos_x, pos_y))

        pygame.display.flip()

    """@staticmethod
    def get_resolution():
        config = configparser.ConfigParser()
        config.read(os.path.join("../../MyPythonGame", "training", "config.ini"))

        height = config['environment']['height']
        width = config['environment']['width']
        return [int(width),int(height)]
    |"""



if __name__ == "__main__":
    game = SimpleGame()
    # test 2
    game.main()

