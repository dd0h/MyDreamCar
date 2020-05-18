import pygame
import constants as c


class Car:
    image = 'MyDreamCar/img/car7.png'
    x = 500
    y = 390
    width = c.CAR_WIDTH
    length = c.CAR_LENGTH

    def display(self):
        return pygame.image.load(self.image)
