import pygame
import color
from constants import *
from random import *

class Obstacle:
    window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    image = 'MyDreamCar/img/car1.png'
    width = CAR_WIDTH
    length = CAR_LENGTH
    change = 0

    def __init__(self, y=9000, x=9000):
        self.x = x
        self.y = y
        self.image = self.randomizeCarStyle()

    def display(self,):
        self.y += 1
        return self.window.blit(pygame.image.load(self.image), (self.x, self.y))

    def randomizeCarStyle(self):
        random_number = randrange(1, 10, 1)
        url = 'MyDreamCar/img/car'
        url += str(random_number)
        url += '.png'
        return url

    def randomizePosition(self, bound_left, bound_right):
        self.x = randrange(int(bound_left), int(bound_right), 1)
        self.y = -CAR_LENGTH
