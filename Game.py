import pygame
from Car import Car
from Road import Road
from ScoreBoard import Score
import color
from constants import *


class Game:
    window = pygame.display.set_mode((WINDOW_HEIGHT, WINDOW_LENGTH))
    score_board = Score()

    def displayThatsOver(self, score):
        self.window.fill(color.WHITE)
        big_font = pygame.font.SysFont('Comic Sans MS', BIG_FONT)
        small_font = pygame.font.SysFont('Comic Sans MS', SMALL_FONT)
        game_over_sign = big_font.render('GAME OVER', False, color.BLACK)
        out_of_road_sign = big_font.render('You are out of road', False, color.BLACK)
        restart_sign = small_font.render('Press space button to restart', False, color.BLACK)
        self.window.blit(game_over_sign, (GAME_OVER_SIGN_X, GAME_OVER_SIGN_Y))
        self.window.blit(out_of_road_sign, (OUT_OF_ROAD_SIGN_X, OUT_OF_ROAD_SIGN_Y))
        self.window.blit(self.score_board.show(), (SCORE_BOARD_X, SCORE_BOARD_Y))
        self.window.blit(restart_sign, (RESTART_SIGN_X, RESTART_SIGN_Y))
        pygame.display.update()

    def Over(self, score):

        self.displayThatsOver(score)

        run = False
        while not run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = True

            keys = pygame.key.get_pressed()
            if keys[pygame.K_SPACE]:
                return self.Run()

    def Run(self):

        self.score_board.setScore(0)
        road = Road(self.score_board)
        car = Car()

        run = True
        while run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

            pygame.time.delay(TIME_DELAY)

            self.Control(car)

            self.window.fill(color.GREEN)

            road.drawRoad(car)

            if road.outOfTheRoad(car) or road.crash(car):
            # if road.outOfTheRoad(car):
                return self.Over(self.score_board.getScore())

            self.window.blit(car.display(), (car.x, car.y))

            self.window.blit(self.score_board.show(), (0, 0))

            pygame.display.update()

    def Control(self, car):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            car.x -= CAR_VELOCITY
        if keys[pygame.K_RIGHT]:
            car.x += CAR_VELOCITY

