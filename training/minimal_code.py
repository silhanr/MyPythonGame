# import pygame module
import pygame, os


class SimpleGame:
    def __init__(self):
        self.root_path = "../../MyPythonGame"

        self.main_screen = None
        self.main_character = \
            pygame.image.load(os.path.join(self.root_path, "images", "big_smile.png"))

        # initialize the pygame module
        pygame.init()

    def main(self):

        self.open_window(860, 640)

        running = True

        # main loop
        while running:
            # event handling, gets all event from the event queue
            for event in pygame.event.get():
                # only do something if the event is of type QUIT
                if event.type == pygame.QUIT:
                    # change the value to False, to exit the main loop
                    running = False

    def open_window(self, height, width):
        """
        This method creates a gaming window
        :param height:
        :param width:
        :return:
        """
        self.main_screen = pygame.display.set_mode((height, width))

        #background
        self.main_screen.blit(
            pygame.image.load(
                os.path.join(self.root_path, "images", "background.jpg")))

        self.main_screen.blit(self.main_character, (100, 100))

        pygame.display.flip()


if __name__ == "__main__":
    game = SimpleGame()
    # test 2
    game.main()
