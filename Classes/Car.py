import constants as c
import pygame


class Car:

    def __init__(self) -> None:
        self.window: pygame.display = pygame.display.set_mode((c.WINDOW_WIDTH, c.WINDOW_HEIGHT))
        self.width: int = c.CAR_WIDTH
        self.length: int = c.CAR_LENGTH

    def display(self) -> pygame.display:
        """Displays car image on the screen."""
        return self.window.blit(pygame.image.load(self.image), (self.x, self.y))
