import pygame
import color
from constants import *
import random

class Obstacle:
    window = pygame.display.set_mode((WINDOW_HEIGHT, WINDOW_LENGTH))
    image = 'MyDreamCar/img/car1.png'
    width = CAR_WIDTH
    length = CAR_LENGTH
    change = 0

    def __init__(self, y=0, x=500, change=0):
        self.x = x
        self.y = y
        self.change = change
        self.image = self.randomizeCarStyle()

    def display(self):
        return self.window.blit(pygame.image.load(self.image), (self.x + self.change, self.y))

    def randomizeCarStyle(self):
        random_number = random.randrange(1, 10, 1)
        url = 'MyDreamCar/img/car'
        url += str(random_number)
        url += '.png'
        return url
