import pygame

import constants as c


class Car:
    window = pygame.display.set_mode((c.WINDOW_WIDTH, c.WINDOW_HEIGHT))
    width = c.CAR_WIDTH
    length = c.CAR_LENGTH

    def display(self):
        return self.window.blit(pygame.image.load(self.image), (self.x, self.y))
