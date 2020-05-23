import pygame
from Classes import Game


def main():
    pygame.init()
    pygame.font.init()
    pygame.display.set_caption("MyDreamCar Beta v21.37")

    game = Game.Game()
    game.Run()

    pygame.quit()


if __name__ == '__main__':
    main()
