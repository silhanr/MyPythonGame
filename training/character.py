import pygame, os, sys, configparser

STEP = 10

class MainCharacter:
    def __init__(self, position_x, position_y):
        self.root_path = "../../MyPythonGame"
        self.character_image = \
            pygame.image.load(os.path.join(self.root_path, "images", "big_smile.png"))

        self.image_size = [50, 50]
        self.resolution = [1000, 500]

        self.position_x = position_x
        self.position_y = position_y



    """
    def get_config(self,section,parameter):
        config = configparser.ConfigParser()
        config.read(os.path.join("self.root_path", "training", "config.ini"))
        return config.read("environment","height")
    """

    def is_in_screen(self, position_x, position_y):
        return (self.resolution[0] - self.image_size[0] >= position_x >= 0) \
               and (self.resolution[1] - self.image_size[1] >= position_y >= 0)

    def move_right(self):
        if self.is_in_screen(self.position_x + STEP, self.position_y):
            self.position_x = self.position_x + STEP
        else:
            print("Border!")

    def move_left(self):
        if self.is_in_screen(self.position_x - STEP, self.position_y):
            self.position_x = self.position_x - STEP
        else:
            print("Border!")

    def hit_space(self):
        print("Space recorded!")
        if self.is_in_screen(self.position_x, self.position_y - STEP)\
                and self.resolution[1] <= self.position_y + self.image_size[1]:
            self.position_y = self.position_y - STEP*2
        else:
            self.position_y = self.resolution[1] - self.image_size[1]


