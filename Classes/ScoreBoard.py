import pygame
import color
import constants as c


class ScoreBoard:

    def __init__(self) -> None:
        pygame.font.init()
        self.score: int = 1
        self.score_font: pygame.font = pygame.font.SysFont('Comic Sans MS', c.SCORE_FONT)

    def show(self) -> pygame.font:
        """Increases score and displays it on the screen."""
        self.score += 1
        return self.score_font.render('score: ' + str(self.score), False, color.BACKGROUND_COLOR)

    def get_score(self) -> int:
        return self.score

    def set_score(self, score: int) -> None:
        self.score = score
