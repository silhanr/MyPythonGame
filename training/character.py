import pygame, os, sys, configparser


class MainCharacter:
    def __init__(self):

        self.root_path = "../../MyPythonGame"
        self.character_image = \
            pygame.image.load(os.path.join(self.root_path, "images", "big_smile.png"))

        self.image_size = [50,50]


        self.position_x = 0
        self.position_y = 0

    """
    def get_config(self,section,parameter):
        config = configparser.ConfigParser()
        config.read(os.path.join("self.root_path", "training", "config.ini"))
        return config.read("environment","height")
    """