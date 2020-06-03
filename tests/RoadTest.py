import constants as c
import unittest

from Classes.Car import Car
from unittest.mock import MagicMock, patch
from Classes.Road import Road
from Classes.ScoreBoard import ScoreBoard


class RoadTest(unittest.TestCase):

    @patch('Classes.ScoreBoard')
    @patch('Classes.Car')
    def setUp(self, mock_score_board, mock_car):
        self.road = Road(mock_score_board)

        self.mock_car = mock_car
        self.mock_car.width = c.CAR_WIDTH
        self.mock_car.length = c.CAR_LENGTH

    def test_out_of_the_road(self):
        self.mock_car.y = 0
        self.mock_car.x = 0
        self.assertTrue(self.road.out_of_the_road(self.mock_car))

        self.mock_car.y = c.CAR_STARTING_X
        self.mock_car.x = c.CAR_STARTING_Y
        self.assertFalse(self.road.out_of_the_road(self.mock_car))

    def test_crash(self):
        self.mock_car.x = c.CAR_STARTING_X
        self.mock_car.y = c.CAR_STARTING_Y

        self.assertFalse(self.road.crash(self.mock_car))

        self.road.obstacles[0].x = c.CAR_STARTING_X + 10
        self.road.obstacles[0].y = c.CAR_STARTING_Y + 10

        self.assertTrue(self.road.crash(self.mock_car))

        self.road.obstacles[1].x = c.CAR_STARTING_X - 10
        self.road.obstacles[1].y = c.CAR_STARTING_Y - 10

        self.assertTrue(self.road.crash(self.mock_car))


if __name__ == '__main__':
    unittest.main()
