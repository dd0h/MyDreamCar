import constants as c
import math

from random import randrange

from Classes.Obstacle import Obstacle
from Classes.ScoreBoard import ScoreBoard
from Classes.WaySegment import WaySegment


class ObstacleGenerator:

    def __init__(self, score) -> None:
        self.score: ScoreBoard = score

    def generate(self, obstacles: [Obstacle], way_segments: [WaySegment]) -> None:
        """
        "Brings back to life" an obstacle which is behind screen by randomizing it's new position.
        Also increases it's velocity
        """
        should_I_wait = randrange(0, c.TRAFFIC_COEFFICIENT, 1)
        if not should_I_wait:
            which_one = randrange(0, c.NUMBER_OF_OBSTACLES, 1)
            if obstacles[which_one].y > c.WINDOW_HEIGHT:
                i = c.WAY_SEGMENT_FIRST
                bound_left = way_segments[i].x_l
                bound_right = way_segments[i].x_r + way_segments[i].x_l - c.CAR_WIDTH
                obstacles[which_one].randomize_position(bound_left, bound_right)
                obstacles[which_one].make_faster(math.log(self.score.get_score(), c.OBSTACLES_ACCELERATION_COEFFICIENT))
