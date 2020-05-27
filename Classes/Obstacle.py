import pygame
import constants as c
from random import randrange
from Classes.Car import Car


class Obstacle(Car):

    def __init__(self, y=c.OBSTACLE_START_POINT, x=c.OBSTACLE_START_POINT):
        self.image = 'MyDreamCar/img/car1.png'
        self.x = x
        self.y = y
        self.image = self.setCarStyle()
        self.velocity = c.OBSTACLE_STARTING_VELOCITY
        super(Obstacle, self).__init__()

    def display(self,):
        self.y += self.velocity
        return self.window.blit(pygame.image.load(self.image), (int(self.x), int(self.y)))

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

    def reset(self):
        self.x = c.OBSTACLE_START_POINT
        self.y = c.OBSTACLE_START_POINT
