import pygame
from Classes.Car import Car
import constants as c


class MyCar(Car):

    def __init__(self):
        self.image = 'MyDreamCar/img/car7.png'
        self.x = c.CAR_STARTING_X
        self.y = c.CAR_STARTING_Y
        super(MyCar, self).__init__()
