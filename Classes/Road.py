import constants as c

from Classes import MapGenerator
from Classes import Obstacle
from Classes import ObstacleGenerator
from Classes import WaySegment
from Classes.Car import Car
from Classes.ScoreBoard import ScoreBoard


class Road:

    def __init__(self, score: ScoreBoard) -> None:
        self.way_segments: [WaySegment] = \
            [WaySegment.WaySegment(int(c.WAY_LENGTH * i), 0) for i in range(c.WAY_SEGMENT_FIRST, c.WAY_SEGMENT_LAST)]

        self.obstacle_generator: ObstacleGenerator = ObstacleGenerator.ObstacleGenerator(score)
        self.obstacles: [Obstacle] = [Obstacle.Obstacle() for i in range(c.NUMBER_OF_OBSTACLES)]

        self.map: MapGenerator = MapGenerator.MapGenerator(score)
        self.map.generate(start_point=0)

    def draw_road(self) -> None:
        """
        Displays way segments and obstacles on screen.
        Also checks if obstacles fall out of the road or overlap and calls proper methods to eliminate these problems.
        """

        self.obstacle_generator.generate(self.obstacles, self.way_segments)

        for i in range(c.WAY_SEGMENT_FIRST, c.WAY_SEGMENT_LAST):
            if self.way_segments[i].y > c.WINDOW_HEIGHT:
                self.way_segments[i] = WaySegment.WaySegment(-c.WAY_LENGTH, self.map.get_next_map_point())
            self.way_segments[i].draw_way()
            self.way_segments[i].y += c.ROAD_SPEED

        for obstacle in self.obstacles:
            if self.out_of_the_road(obstacle) or self.crash(obstacle):
                obstacle.reset()
            obstacle.display()

    def out_of_the_road(self, car: Car) -> bool:
        """Checks if car had fallen out of the road."""
        for i in range(c.WAY_SEGMENT_FIRST, c.WAY_SEGMENT_LAST):
            if car.y <= self.way_segments[i].y and self.way_segments[i - 1].out_of_the_way_segment(car):
                return True
        return False

    def crash(self, car: Car) -> bool:
        """Checks if car had contact with obstacles."""
        for i in range(c.NUMBER_OF_OBSTACLES):
            if (
                    (self.obstacles[i].x < car.x < self.obstacles[i].x + self.obstacles[i].width
                     and self.obstacles[i].y < car.y < self.obstacles[i].y + self.obstacles[i].length)
                    or (self.obstacles[i].x < car.x + car.width <= self.obstacles[i].x + self.obstacles[i].width
                        and self.obstacles[i].y < car.y < self.obstacles[i].y + self.obstacles[i].length)
                    or (self.obstacles[i].x < car.x < self.obstacles[i].x + self.obstacles[i].width
                        and self.obstacles[i].y < car.y + car.length < self.obstacles[i].y + self.obstacles[i].length)
                    or (self.obstacles[i].x < car.x + car.width < self.obstacles[i].x + self.obstacles[i].width
                        and self.obstacles[i].y < car.y < self.obstacles[i].y + self.obstacles[i].length)
                    or (self.obstacles[i].x < car.x + car.width / 2 < self.obstacles[i].x + self.obstacles[i].width
                        and self.obstacles[i].y < car.y < self.obstacles[i].y + self.obstacles[i].length)
                    or (self.obstacles[i].x < car.x + car.width / 2 < self.obstacles[i].x + self.obstacles[i].width
                        and self.obstacles[i].y < car.y + car.length < self.obstacles[i].y + self.obstacles[i].length)
            ):
                return True
        return False
