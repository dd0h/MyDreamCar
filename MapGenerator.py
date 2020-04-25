import random
import constants as c
import math

class MapGenerator:

    current_map_point = 0

    def __init__(self, score):
        self.map_length = c.MAP_LENGTH
        self.score = score

    def generate(self, start_point):
        self.map_points = [start_point for i in range(self.map_length)]
        current_segment = 0

        while current_segment <= self.map_length - c.SAFE_EXCESS:
            howMuchSegmentsToSide = random.randrange(1, 20, 1)
            max_curvature = math.log(self.score.getScore() + 1, 7)
            if max_curvature > 15:
                max_curvature = 15
            #print(max_curvature)
            curvature = round(random.uniform(-max_curvature, max_curvature), 1)

            for j in range(current_segment, current_segment + howMuchSegmentsToSide):
                if current_segment + howMuchSegmentsToSide <= self.map_length:
                    while not (c.MAX_LEFT_DEVIATION_OF_ROAD  < self.map_points[j] + curvature < c.MAX_RIGHT_DEVIATION_OF_ROAD ):
                        curvature = random.randrange(0, 5, 1)
                    self.map_points[j + 1] = self.map_points[j] + curvature

            current_segment += howMuchSegmentsToSide

    def getNextMapPoint(self):
        if self.current_map_point > self.map_length - c.SAFE_EXCESS:
            self.generate(self.map_points[self.current_map_point])
            self.current_map_point = 0
        self.current_map_point += 1
        return self.map_points[self.current_map_point]
