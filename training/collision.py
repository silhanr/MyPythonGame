import threading, pygame
from pygame import Rect
from threading import Thread

RECT_SIZE = 50

class CollisionObjects(Thread):





    def run(self):
        targets = []
        for i in range(1):
            target = Rect(0, 0, RECT_SIZE, RECT_SIZE)
            targets.append(target)


        #for target in self.targets:
        #    pygame.draw.rect(self.game_screen, (255, 1, 1), target)
        #pygame.display.update()



