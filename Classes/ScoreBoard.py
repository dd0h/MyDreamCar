import pygame
import color
import constants as c


class ScoreBoard:

    def __init__(self):
        pygame.font.init()
        self.score = 0
        self.score_font = pygame.font.SysFont('Comic Sans MS', c.SCORE_FONT)

    def show(self):
        self.score += 1
        return self.score_font.render('score: ' + str(self.score), False, color.BLACK)

    def getScore(self):
        return self.score

    def setScore(self, score):
        self.score = score
