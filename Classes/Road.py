from random import randrange

from Classes import ObstacleGenerator
import constants as c
from Classes import WaySegment
from Classes import Obstacle
from Classes import MapGenerator


class Road:

    def __init__(self, score):
        self.way_segments = [WaySegment.WaySegment(c.WAY_LENGTH * i, 0) for i in range(c.WAY_SEGMENT_FIRST, c.WAY_SEGMENT_LAST)]

        self.obstacleGenerator = ObstacleGenerator.ObstacleGenerator(score)
        self.obstacles = [self.obstacleGenerator.createObstacle() for i in range(c.NUMBER_OF_OBSTACLES)]

        self.map = MapGenerator.MapGenerator(score)
        self.map.generate(start_point=0)

    def drawRoad(self, car):

        self.obstacleGenerator.generate(self.obstacles, self.way_segments)

        for i in range(c.WAY_SEGMENT_FIRST, c.WAY_SEGMENT_LAST):
            if self.way_segments[i].y > c.WINDOW_HEIGHT:
                self.way_segments[i] = WaySegment.WaySegment(-c.WAY_LENGTH, self.map.getNextMapPoint())
            self.way_segments[i].drawWay()
            self.way_segments[i].y += c.ROAD_SPEED

        for obstacle in self.obstacles:
            obstacle.display()

    def outOfTheRoad(self, car):
        for i in range(c.WAY_SEGMENT_FIRST, c.WAY_SEGMENT_LAST):
            if car.y <= self.way_segments[i].y and self.way_segments[i - 1].outOfTheWaySegment(car):
                return True

    def crash(self, car):
        for i in range(c.NUMBER_OF_OBSTACLES):
            if (
                    (self.obstacles[i].x < car.x < self.obstacles[i].x + self.obstacles[i].width
                     and self.obstacles[i].y < car.y < self.obstacles[i].y + self.obstacles[i].length)
                    or (self.obstacles[i].x < car.x + car.width < self.obstacles[i].x + self.obstacles[i].width
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
