import unittest

import pygame
import constants as c

from Classes.ScoreBoard import ScoreBoard


class ScoreBoard_test(unittest.TestCase):

    def setUp(self):
        self.score_board = ScoreBoard()

    def test_show(self):
        self.assertIsNotNone(self.score_board.show())

    def test_getScore(self):
        self.assertIsInstance(self.score_board.getScore(), int)

    def test_setScore(self):
        self.assertIsNone(self.score_board.setScore(0))


if __name__ == '__main__':
    unittest.main()
