import constants as c
from WaySegment import WaySegment
from Obstacle import Obstacle
from MapGenerator import MapGenerator


class Road:

    def __init__(self, score):
        self.ws = [WaySegment(c.WAY_LENGTH * i, 0) for i in range(c.WAY_SEGMENT_FIRST, c.WAY_SEGMENT_LAST)]
        self.obstacle = Obstacle()

        self.map = MapGenerator(score)
        self.map.generate(start_point=0)

    def drawRoad(self, car):
        for i in range(c.WAY_SEGMENT_FIRST, c.WAY_SEGMENT_LAST):
            if self.ws[i].y > c.WINDOW_LENGTH:
                self.ws[i] = WaySegment(-c.WAY_LENGTH, self.map.getNextMapPoint())
            self.ws[i].drawWay()
            self.ws[i].y += c.SPEED

        #todo drawing obstacles
            # self.obstacle.display()
            # self.obstacle.y += 0.5  # temporary

    def outOfTheRoad(self, car):
        for i in range(c.WAY_SEGMENT_FIRST, c.WAY_SEGMENT_LAST):
            if car.y <= self.ws[i].y and self.ws[i - 1].outOfTheWaySegment(car):
                return True
