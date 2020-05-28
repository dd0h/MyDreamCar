import pygame
from Classes import MyCar
from Classes import Road
from Classes import ScoreBoard
import color
import constants as c


class Game:

    def __init__(self):
        self.window = pygame.display.set_mode((c.WINDOW_WIDTH, c.WINDOW_HEIGHT))
        self.score_board = ScoreBoard.ScoreBoard()

    def display_thats_over(self, score):
        """Displays "thats over" window."""
        self.window.fill(color.WHITE)
        big_font = pygame.font.SysFont('Comic Sans MS', c.BIG_FONT)
        small_font = pygame.font.SysFont('Comic Sans MS', c.SMALL_FONT)
        game_over_sign = big_font.render('GAME OVER', False, color.BLACK)
        out_of_road_sign = big_font.render('You are out of road', False, color.BLACK)
        restart_sign = small_font.render('Press space button to restart', False, color.BLACK)
        self.window.blit(game_over_sign, (c.GAME_OVER_SIGN_X, c.GAME_OVER_SIGN_Y))
        self.window.blit(out_of_road_sign, (c.OUT_OF_ROAD_SIGN_X, c.OUT_OF_ROAD_SIGN_Y))
        self.window.blit(self.score_board.show(), (c.SCORE_BOARD_X, c.SCORE_BOARD_Y))
        self.window.blit(restart_sign, (c.RESTART_SIGN_X, c.RESTART_SIGN_Y))
        pygame.display.update()

    def over(self, score):
        """Calls display_thats_over() and restarts game after SPACE key pressed."""
        self.display_thats_over(score)

        run = False
        while not run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = True

            keys = pygame.key.get_pressed()
            if keys[pygame.K_SPACE]:
                return self.run()

    def run(self):
        """Initializes core components and manages them."""
        self.score_board.set_score(0)
        road = Road.Road(self.score_board)
        car = MyCar.MyCar()

        run = True
        while run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

            pygame.time.delay(c.TIME_DELAY)

            self.control(car)

            self.window.fill(color.GREEN)

            road.draw_road(car)

            if road.out_of_the_road(car) or road.crash(car):
                return self.over(self.score_board.get_score())

            car.display()

            self.window.blit(self.score_board.show(), (0, 0))

            pygame.display.update()

    def control(self, car):
        """Changes car position according to key pressed"""
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            car.x -= c.CAR_VELOCITY
        if keys[pygame.K_RIGHT]:
            car.x += c.CAR_VELOCITY

