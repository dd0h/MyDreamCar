import pygame
import color
import constants as c

class ScoreBoard:
    score = 0

    pygame.font.init()
    score_font = pygame.font.SysFont('Comic Sans MS', c.SCORE_FONT)

    def show(self):
        self.score += 1
        return self.score_font.render('score: ' + str(self.score), False, color.BLACK)
