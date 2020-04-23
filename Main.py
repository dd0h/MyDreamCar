import pygame
from Game import Game

pygame.init()
pygame.font.init()
pygame.display.set_caption("MyDreamCar Beta v21.37")

game = Game()
game.Run()

pygame.quit()