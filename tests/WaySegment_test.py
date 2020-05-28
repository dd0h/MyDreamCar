import unittest

from Classes.Car import Car
from Classes.WaySegment import WaySegment
from unittest.mock import MagicMock, patch
import constants as c


class WaySegment_test(unittest.TestCase):

    @patch('Classes.Car')
    def setUp(self, mock_Car):
        self.way_segment = WaySegment(0, 0)
        self.mock_Car = mock_Car
        self.mock_Car.width = c.CAR_WIDTH

    def test_draw_way(self):
        self.assertIsNone(self.way_segment.draw_way())

    def test_out_of_the_way_segment(self):
        self.mock_Car.x = c.CAR_STARTING_X
        self.mock_Car.y = 0
        self.assertFalse(self.way_segment.out_of_the_way_segment(self.mock_Car))

        self.mock_Car.x = self.way_segment.x_l + c.ROAD_WIDTH
        self.assertTrue(self.way_segment.out_of_the_way_segment(self.mock_Car))


if __name__ == '__main__':
    unittest.main()
