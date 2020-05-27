import unittest

from Classes.Car import Car
from Classes.Road import Road
from Classes.ScoreBoard import ScoreBoard
from unittest.mock import MagicMock, patch
import constants as c


class Road_test(unittest.TestCase):

    @patch('Classes.ScoreBoard')
    @patch('Classes.Car')
    def setUp(self, mock_ScoreBoard, mock_Car):
        self.road = Road(mock_ScoreBoard)

        self.mock_Car = mock_Car
        self.mock_Car.width = c.CAR_WIDTH
        self.mock_Car.length = c.CAR_LENGTH

    def test_drawRoad(self):
        self.assertIsNone(self.road.drawRoad(self.mock_Car))

    def test_outOfTheRoad(self):
        self.mock_Car.y = 0
        self.mock_Car.x = 0
        self.assertTrue(self.road.outOfTheRoad(self.mock_Car))

        self.mock_Car.y = c.CAR_STARTING_X
        self.mock_Car.x = c.CAR_STARTING_Y
        self.assertFalse(self.road.outOfTheRoad(self.mock_Car))

    def test_crash(self):

        self.mock_Car.x = c.CAR_STARTING_X
        self.mock_Car.y = c.CAR_STARTING_Y

        self.assertFalse(self.road.crash(self.mock_Car))

        self.road.obstacles[0].x = c.CAR_STARTING_X + 10
        self.road.obstacles[0].y = c.CAR_STARTING_Y + 10

        self.assertTrue(self.road.crash(self.mock_Car))

        self.road.obstacles[1].x = c.CAR_STARTING_X - 10
        self.road.obstacles[1].y = c.CAR_STARTING_Y - 10

        self.assertTrue(self.road.crash(self.mock_Car))


if __name__ == '__main__':
    unittest.main()
