import pygame


class Car:
    image = 'MyDreamCar/img/car1.png'
    x = 500
    y = 390
    width = 40
    length = 102

    def display(self):
        return pygame.image.load(self.image)
