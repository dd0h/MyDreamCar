import unittest

import pygame
import constants as c

from Classes.ScoreBoard import ScoreBoard


class ScoreBoard_test(unittest.TestCase):

    def setUp(self):
        self.score_board = ScoreBoard()

    def test_show(self):
        self.assertIsNotNone(self.score_board.show())

    def test_get_score(self):
        self.assertIsInstance(self.score_board.get_score(), int)

    def test_set_score(self):
        self.assertIsNone(self.score_board.set_score(0))


if __name__ == '__main__':
    unittest.main()
