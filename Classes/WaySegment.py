import color
import constants as c
import pygame


class WaySegment:
    window = pygame.display.set_mode((c.WINDOW_WIDTH, c.WINDOW_HEIGHT))

    def __init__(self, y, x):
        self.x_l = (c.WINDOW_WIDTH - c.ROAD_WIDTH) / 2  # Up left corner position
        self.x_r = c.ROAD_WIDTH + c.ROAD_BORDER_SIZE  # Up right corner position

        self.x_l += x
        self.y = y

    def draw_way(self):
        """Displays a single way segment on the screen."""
        way = (int(self.x_l), int(self.y), int(self.x_r), c.WAY_LENGTH)
        pygame.draw.rect(self.window, color.ROAD_COLOR, way)
        left_border_line = (int(self.x_l), int(self.y), c.ROAD_BORDER_SIZE, c.WAY_LENGTH)
        right_border_line = (int(self.x_l) + c.ROAD_WIDTH, self.y, c.ROAD_BORDER_SIZE, c.WAY_LENGTH)
        pygame.draw.rect(self.window, color.BACKGROUND_COLOR, left_border_line)
        pygame.draw.rect(self.window, color.BACKGROUND_COLOR, right_border_line)

    def out_of_the_way_segment(self, car):
        """Checks if the car has gone off the way segment"""
        if car.x < self.x_l - c.OUTSIDE_BORDER or car.x > self.x_l + self.x_r - car.width + c.OUTSIDE_BORDER:
            return True
        return False
