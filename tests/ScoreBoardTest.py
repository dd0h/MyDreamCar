import unittest

from Classes.ScoreBoard import ScoreBoard


class ScoreBoardTest(unittest.TestCase):

    def setUp(self):
        self.score_board = ScoreBoard()

    def test_show(self):
        self.assertIsNotNone(self.score_board.show())

    def test_set_and_get_score(self):
        value = 0
        self.score_board.set_score(value)
        self.assertEquals(self.score_board.get_score(), value)


if __name__ == '__main__':
    unittest.main()
