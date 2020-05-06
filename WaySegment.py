import pygame
import color
from constants import *

class WaySegment:
    x_l = (WINDOW_HEIGHT - ROAD_WIDTH) / 2 # Up left corner position
    x_r = ROAD_WIDTH + ROAD_BORDER_SIZE  # Up right corner position
    window = pygame.display.set_mode((WINDOW_HEIGHT, WINDOW_LENGTH))

    def __init__(self, y, x):
        self.x_l += x
        self.y = y

    def drawWay(self):
        way = (self.x_l, self.y, self.x_r, WAY_LENGTH)
        pygame.draw.rect(self.window, color.WHITE, way)
        left_border_line = (self.x_l, self.y, ROAD_BORDER_SIZE, WAY_LENGTH)
        right_border_line = (self.x_l + ROAD_WIDTH, self.y, ROAD_BORDER_SIZE, WAY_LENGTH)
        pygame.draw.rect(self.window, color.BLACK, left_border_line)
        pygame.draw.rect(self.window, color.BLACK, right_border_line)

    def outOfTheWaySegment(self, car):
        if car.x < self.x_l - 10 or car.x > self.x_l + self.x_r - car.width + 10:
            return True
        return False