# import pygame module
import time

import pygame, os, configparser
from pygame.rect import Rect

from training.character import MainCharacter
from training.collision import CollisionObjects
from training.hook import Hook


FPS = 60
HOOK_WIDTH = 5
HOOK_HEIGHT = 10
GROW_INTERVAL = 100
RECT_SIZE = 50

class SimpleGame:
    def __init__(self):
        self.root_path = "../../MyPythonGame"

        # self.game_character = MainCharacter(475, 450)
        self.game_character = MainCharacter(475, 450)

        self.hook = self.reset_hook()

        self.game_screen = None
        self.resolution = [1000, 500]

        self.clock = pygame.time.Clock()

        # initialize the pygame module
        pygame.init()

    def main(self):

        self.open_window(self.resolution[0], self.resolution[1])

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
                        self.reload_background()

                        self.game_screen.blit(self.game_character.character_image,
                                              (self.game_character.position_x, \
                                               self.game_character.position_y))


                        #Extend hook until it reaches top of screen
                        while self.hook.top >= 0:
                            self.hook.shot(self.game_character)
                            pygame.time.wait(GROW_INTERVAL)

                            pygame.draw.rect(self.game_screen, 5, self.hook, HOOK_WIDTH)
                            pygame.display.update()




                    self.reload_background()
                    self.game_screen.blit(self.game_character.character_image,
                                          (self.game_character.position_x, \
                                           self.game_character.position_y))

                # Reset Hook
                self.hook = self.reset_hook()

                # Draw rectangle
                pygame.draw.rect(self.game_screen, 5, self.hook, HOOK_WIDTH)

            self.clock.tick(FPS)



            pygame.display.update()


    def open_window(self, width, height):
        """
        This method creates a gaming window
        :param height:
        :param width:
        :return:
        """
        self.game_screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption("Shoot the square!")

        # display background
        self.reload_background()

        self.game_screen.blit(self.game_character.character_image,
                              (self.game_character.position_x,
                               self.game_character.position_y))

        pygame.display.flip()


    def reset_hook(self):
        hook = Hook( \
            self.game_character.position_x + self.game_character.image_size[0] / 2, \
            1, 1, HOOK_HEIGHT)
        hook.center_hook(self.game_character)
        return hook

    def reload_background(self):
        self.game_screen.blit(
            pygame.image.load(
                os.path.join(self.root_path, "images", "background.jpg")), (0, 0))




if __name__ == "__main__":
    game = SimpleGame()
    game.main()



