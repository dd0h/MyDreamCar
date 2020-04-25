import pygame
import color
import constants as c

class Score:
    score = 0

    pygame.font.init()
    score_font = pygame.font.SysFont('Comic Sans MS', c.SCORE_FONT)

    def show(self):
        self.score += 1
        return self.score_font.render('score: ' + str(self.score), False, color.BLACK)

    def getScore(self):
        return self.score

    def setScore(self, score):
        self.score = score
