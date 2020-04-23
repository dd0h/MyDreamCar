import random
import constants as c

class MapGenerator:

    current_map_point = 0

    def __init__(self):
        self.map_length = c.MAP_LENGTH

    def generate(self, start_point):
        self.map_points = [start_point for i in range(self.map_length)]
        current_segment = 0

        while current_segment <= self.map_length - c.SAFE_EXCESS:

            howMuchSegmentsToSide = random.randrange(1, 20, 1)
            curvature = random.randrange(-5, 5, 1)

            for j in range(current_segment, current_segment + howMuchSegmentsToSide):
                if current_segment + howMuchSegmentsToSide <= self.map_length:
                    while not (-350 < self.map_points[j] + curvature < 340):
                        curvature = random.randrange(0, 5, 1)
                    self.map_points[j + 1] = self.map_points[j] + curvature

            current_segment += howMuchSegmentsToSide

    def getNextMapPoint(self):
        if self.current_map_point > self.map_length - c.SAFE_EXCESS:
            self.generate(self.map_points[self.current_map_point])
            self.current_map_point = 0
        self.current_map_point += 1
        return self.map_points[self.current_map_point]
