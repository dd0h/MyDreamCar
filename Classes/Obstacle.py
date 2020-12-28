import constants as c
import pygame

from Classes.Car import Car
from random import randrange


class Obstacle(Car):

    def __init__(self, y: int = c.OBSTACLE_START_POINT, x: int = c.OBSTACLE_START_POINT) -> None:
        self.image: str = 'MyDreamCar/img/car1.png'
        self.x: int = x
        self.y: int = y
        self.image: str = self.set_car_style()
        self.velocity: float = c.OBSTACLE_STARTING_VELOCITY
        super(Obstacle, self).__init__()

    def display(self) -> pygame.display:
        """Changes y position of obstacle and displays obstacle image on the screen."""
        self.y += self.velocity
        return self.window.blit(pygame.image.load(self.image), (int(self.x), int(self.y)))

    def set_car_style(self) -> str:
        """Randoms and returns path of obstacle's image."""
        img_number = randrange(0, 10, 1)
        url = 'MyDreamCar/img/car'
        url += str(img_number)
        url += '.png'
        return url

    def randomize_position(self, bound_left: int, bound_right: int) -> None:
        """Randomizes position on the road."""
        self.x = randrange(int(bound_left), int(bound_right), 1)
        self.y = -c.CAR_LENGTH
        self.set_car_style()

    def make_faster(self, how_much: float) -> None:
        """Increases velocity of obstacle."""
        self.velocity += how_much

    def reset(self) -> None:
        """Sets default position."""
        self.x = c.OBSTACLE_START_POINT
        self.y = c.OBSTACLE_START_POINT
