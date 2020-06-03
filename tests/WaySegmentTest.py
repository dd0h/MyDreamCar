import constants as c
import unittest

from Classes.Car import Car
from unittest.mock import MagicMock, patch
from Classes.WaySegment import WaySegment


class WaySegmentTest(unittest.TestCase):

    @patch('Classes.Car')
    def setUp(self, mock_car):
        self.way_segment = WaySegment(0, 0)
        self.mock_car = mock_car
        self.mock_car.width = c.CAR_WIDTH

    def test_draw_way(self):
        self.assertIsNone(self.way_segment.draw_way())

    def test_out_of_the_way_segment(self):
        self.mock_car.x = c.CAR_STARTING_X
        self.mock_car.y = 0
        self.assertFalse(self.way_segment.out_of_the_way_segment(self.mock_car))

        self.mock_car.x = self.way_segment.x_l + c.ROAD_WIDTH
        self.assertTrue(self.way_segment.out_of_the_way_segment(self.mock_car))


if __name__ == '__main__':
    unittest.main()
