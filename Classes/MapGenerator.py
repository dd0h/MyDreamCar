import constants as c
import math
import random

from Classes.ScoreBoard import ScoreBoard


class MapGenerator:

    def __init__(self, score: ScoreBoard) -> None:
        self.current_map_point: int = 0
        self.map_length: int = c.MAP_LENGTH
        self.score: ScoreBoard = score
        self.map_points: [int] = []

    def generate(self, start_point: int) -> None:
        """Fills the table self.map_points with points corresponding to the position of the way segment on the map."""
        self.map_points = [start_point for i in range(self.map_length)]
        current_segment = 0

        while current_segment <= self.map_length - c.SAFE_EXCESS:
            how_much_segments_to_side = random.randrange(c.MIN_SEGMENTS_TO_SIDE, c.MAX_SEGMENTS_TO_SIDE, 1)
            max_curvature = math.log(self.score.get_score() + 1, c.MAX_CURVATURE_COEFFICIENT)
            if max_curvature > c.MAX_CURVATURE:
                max_curvature = c.MAX_CURVATURE
            curvature = round(random.uniform(-max_curvature, max_curvature), 1)

            for j in range(current_segment, current_segment + how_much_segments_to_side):
                if current_segment + how_much_segments_to_side <= self.map_length:
                    while not (
                            c.MAX_LEFT_DEVIATION_OF_ROAD < self.map_points[
                        j] + curvature < c.MAX_RIGHT_DEVIATION_OF_ROAD):
                        curvature = round(random.uniform(-max_curvature, max_curvature), 1)
                    self.map_points[j + 1] = self.map_points[j] + curvature

            current_segment += how_much_segments_to_side

    def get_next_map_point(self) -> int:
        """
        Returns single map point and calls generate() to refill array with new map points
        when the end of array is being reached.
         """
        if self.current_map_point > self.map_length - c.SAFE_EXCESS:
            self.generate(self.map_points[self.current_map_point])
            self.current_map_point = 0
        self.current_map_point += 1
        return self.map_points[self.current_map_point]
