import pygame
import color
import constants as c

class Obstacle:
    window = pygame.display.set_mode((c.WINDOW_HEIGHT, c.WINDOW_LENGTH))
    image = 'MyDreamCar/img/car1.png'
    width = 40
    length = 102
    change = 0

    def __init__(self, y=0, x=500, change=0):
        self.x = x
        self.y = y
        self.change = change

    def display(self):
        return self.window.blit(pygame.image.load(self.image), (self.x + self.change, self.y))

    def crash(self):
        pass # todo
