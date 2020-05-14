from Obstacle import *
from random import *

class ObstacleGenerator:

    def __init__(self, score):
        self.score = score

    def generate(self):
        return Obstacle()
