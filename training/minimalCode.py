# import pygame module
import pygame


class SimpleGame:
    def __init__(self):
        self.screen = None

    def main(self):

        self.open_window(860,640)

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
        self.screen = pygame.display.set_mode((height, width))


if __name__ == "__main__":
    game = SimpleGame()
    # test 2
    game.main()
