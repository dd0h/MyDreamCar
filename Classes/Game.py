import color
import constants as c
import pygame

from Classes import MyCar
from Classes import Road
from Classes import ScoreBoard



class Game:

    def __init__(self) -> None:
        self.window: pygame.display = pygame.display.set_mode((c.WINDOW_WIDTH, c.WINDOW_HEIGHT))
        self.score_board: ScoreBoard = ScoreBoard.ScoreBoard()

    def display_thats_over(self) -> None:
        """Displays "thats over" window."""
        self.window.fill(color.BORDER_COLOR)
        big_font = pygame.font.SysFont('Comic Sans MS', c.BIG_FONT)
        small_font = pygame.font.SysFont('Comic Sans MS', c.SMALL_FONT)
        game_over_sign = big_font.render('GAME OVER', False, color.BACKGROUND_COLOR)
        out_of_road_sign = big_font.render('You are out of road', False, color.BACKGROUND_COLOR)
        restart_sign = small_font.render('Press space button to restart', False, color.BACKGROUND_COLOR)
        self.window.blit(game_over_sign, (c.GAME_OVER_SIGN_X, c.GAME_OVER_SIGN_Y))
        self.window.blit(out_of_road_sign, (c.OUT_OF_ROAD_SIGN_X, c.OUT_OF_ROAD_SIGN_Y))
        self.window.blit(self.score_board.show(), (c.SCORE_BOARD_X, c.SCORE_BOARD_Y))
        self.window.blit(restart_sign, (c.RESTART_SIGN_X, c.RESTART_SIGN_Y))
        pygame.display.update()

    def over(self) -> None:
        """Calls display_thats_over() and restarts game after SPACE key pressed."""
        self.display_thats_over()

        run = False
        while not run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = True

            keys = pygame.key.get_pressed()
            if keys[pygame.K_SPACE]:
                return self.run()

    def run(self) -> None:
        """Initializes core components and manages them."""
        self.score_board.set_score(1)
        road = Road.Road(self.score_board)
        car = MyCar.MyCar()

        run = True
        while run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

            pygame.time.delay(c.TIME_DELAY)

            self.control(car)

            self.window.fill(color.GRASS_COLOR)

            road.draw_road()

            if road.out_of_the_road(car) or road.crash(car):
                return self.over()

            car.display()

            self.window.blit(self.score_board.show(), (0, 0))

            pygame.display.update()

    def control(self, my_car: MyCar) -> None:
        """Changes car position according to key pressed"""
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            my_car.x -= c.CAR_VELOCITY
        if keys[pygame.K_RIGHT]:
            my_car.x += c.CAR_VELOCITY

