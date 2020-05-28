import pygame
import color
import constants as c


class ScoreBoard:

    def __init__(self):
        pygame.font.init()
        self.score = 0
        self.score_font = pygame.font.SysFont('Comic Sans MS', c.SCORE_FONT)

    def show(self):
        """Increases score and displays it on the screen."""
        self.score += 1
        return self.score_font.render('score: ' + str(self.score), False, color.BLACK)

    def get_score(self):
        return self.score

    def set_score(self, score):
        self.score = score
