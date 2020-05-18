import pygame
import constants as c
from random import randrange

class Obstacle:
    window = pygame.display.set_mode((c.WINDOW_WIDTH, c.WINDOW_HEIGHT))
    image = 'MyDreamCar/img/car1.png'
    width = c.CAR_WIDTH
    length = c.CAR_LENGTH
    velocity = c.OBSTACLE_STARTING_VELOCITY

    def __init__(self, y=9000, x=9000):
        self.x = x
        self.y = y
        self.image = self.setCarStyle()

    def display(self,):
        self.y += self.velocity
        return self.window.blit(pygame.image.load(self.image), (self.x, self.y))

    def setCarStyle(self):
        img_number = randrange(0, 10, 1)
        url = 'MyDreamCar/img/car'
        url += str(img_number)
        url += '.png'
        return url

    def randomizePosition(self, bound_left, bound_right):
        self.x = randrange(int(bound_left), int(bound_right), 1)
        self.y = -c.CAR_LENGTH
        self.setCarStyle()

    def makeFaster(self, how_much):
        self.velocity += how_much
