from abc import ABC, abstractmethod

import constants as c
import pygame


class Car(ABC):

    def __init__(self) -> None:
        self.window: pygame.display = pygame.display.set_mode((c.WINDOW_WIDTH, c.WINDOW_HEIGHT))
        self.width: int = c.CAR_WIDTH
        self.length: int = c.CAR_LENGTH
        self.x: int = 0
        self.y: int = 0
        self.image: str = ""

    @abstractmethod
    def display(self) -> pygame.display:
        """Displays car image on the screen."""
        pass
