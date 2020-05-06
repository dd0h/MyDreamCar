import pygame
from constants import *


class Car:
    image = 'MyDreamCar/img/car7.png'
    x = 500
    y = 390
    width = CAR_WIDTH
    length = CAR_LENGTH

    def display(self):
        return pygame.image.load(self.image)
