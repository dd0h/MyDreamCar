import math
from random import randrange
import constants as c
from Classes import Obstacle

class ObstacleGenerator:

    def __init__(self, score):
        self.score = score

    def createObstacle(self):
        return Obstacle.Obstacle()

    def generate(self, obstacles, way_segments):
        should_I_wait = randrange(0, c.TRAFFIC_COEFFICIENT, 1)
        if not should_I_wait:
            which_one = randrange(0, c.NUMBER_OF_OBSTACLES, 1)
            if obstacles[which_one].y > c.WINDOW_HEIGHT:
                i = c.WAY_SEGMENT_FIRST
                bound_left = way_segments[i].x_l
                bound_right = way_segments[i].x_r + way_segments[i].x_l - c.CAR_WIDTH
                obstacles[which_one].randomizePosition(bound_left, bound_right)
                obstacles[which_one].makeFaster(math.log(self.score.getScore(), c.OBSTACLES_ACCELERATION_COEFFICIENT))
