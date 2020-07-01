import pygame

from Classes import Game


def main():
    pygame.init()
    pygame.display.set_caption("MyDreamCar v.1.0")

    game = Game.Game()
    game.run()

    pygame.quit()


if __name__ == '__main__':
    main()
