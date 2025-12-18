# Maze Game
import pygame
from rich import print
from sys import exit as quit

CELLSIZE = 25

class player():
    def __init__(self, x: int, y: int) -> None:
        self.pos = [x, y]
        self.moveDistance = CE;;SIZE

    def movement(self) -> None:
        pass

class platform():
    def __init__(self, xMul: int, yMul: int) -> None:
        self.size: int = CELLSIZE
        self.pos = [xMul * self.size, yMul * self.size]

def Draw():
    pass

pygame.init()

windowSize: tuple[int, int] = (800, 600)

Window = pygame.display.set_mode(windowSize)
pygame.display.set_caption("Maze game")

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit('Quit the game!')
            
    Window.fill((45, 12, 43))

    pygame.display.update()