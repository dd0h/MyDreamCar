import pygame

import constants as c


class Car:

    def __init__(self):
        self.window = pygame.display.set_mode((c.WINDOW_WIDTH, c.WINDOW_HEIGHT))
        self.width = c.CAR_WIDTH
        self.length = c.CAR_LENGTH

    def display(self):
        return self.window.blit(pygame.image.load(self.image), (self.x, self.y))
