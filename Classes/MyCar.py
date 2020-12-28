import pygame

import constants as c

from Classes.Car import Car


class MyCar(Car):

    def __init__(self) -> None:
        super(MyCar, self).__init__()
        self.image: str = 'MyDreamCar/img/car7.png'
        self.x: int = c.CAR_STARTING_X
        self.y: int = c.CAR_STARTING_Y

    def display(self) -> pygame.display:
        """Displays car image on the screen."""
        return self.window.blit(pygame.image.load(self.image), (self.x, self.y))
