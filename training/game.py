# import pygame module
import time

import pygame, os, configparser

from training.character import MainCharacter

FPS = 60


class SimpleGame:
    def __init__(self):
        self.root_path = "../../MyPythonGame"

        self.game_screen = None
        self.resolution = [1000, 500]
        # self.game_character = MainCharacter(475, 450)
        self.game_character = MainCharacter(475, 450)
        self.clock = pygame.time.Clock()

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
                if event.type == pygame.QUIT \
                        or (event.type == pygame.KEYDOWN and event.key == pygame.K_q):
                    # change the value to False, to exit the main loop
                    running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        print("move ->")
                        self.game_character.move_right()
                    if event.key == pygame.K_LEFT:
                        print("move <-")
                        self.game_character.move_left()
                    if event.key == pygame.K_SPACE:
                        print("space")
                        self.game_character.hit_space()
                        self.reload_background()

                        self.game_screen.blit(self.game_character.character_image,
                                              (self.game_character.position_x, \
                                               self.game_character.position_y))

                        # self.clock.tick(FPS)

                        pygame.display.update()

                        for i in range(5):
                            self.clock.tick(FPS)

                        self.game_character.hit_space()

                    self.reload_background()
                    self.game_screen.blit(self.game_character.character_image,
                                          (self.game_character.position_x, \
                                           self.game_character.position_y))

            self.clock.tick(FPS)
            pygame.display.update()

            """if self.main_character.position_x > \
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
            """

    def open_window(self, width, height):
        """
        This method creates a gaming window
        :param height:
        :param width:
        :return:
        """
        self.game_screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption("Shoot the ball!")

        # display background
        self.reload_background()

        self.game_screen.blit(self.game_character.character_image,
                              (self.game_character.position_x,
                               self.game_character.position_y))

        pygame.display.flip()

    """@staticmethod
    def get_resolution():
        config = configparser.ConfigParser()
        config.read(os.path.join("../../MyPythonGame", "training", "config.ini"))

        height = config['environment']['height']
        width = config['environment']['width']
        return [int(width),int(height)]
    |"""

    def reload_background(self):
        self.game_screen.blit(
            pygame.image.load(
                os.path.join(self.root_path, "images", "background.jpg")), (0, 0))


if __name__ == "__main__":
    game = SimpleGame()
    # test 2
    game.main()
