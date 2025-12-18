# Maze Game
import pygame
from rich import print
from sys import exit as quit


class Player():
    def __init__(self, x: int, y: int) -> None:
        self.x: int = x * CELLSIZE
        self.y: int = y * CELLSIZE
        self.moveDistance: int = CELLSIZE
        self.allowMove: bool = True
    
    def detectkeyboard(self) -> None:
        keyboard = pygame.key.get_pressed()
        if self.allowMove:
            if keyboard[pygame.K_a]:
                self.x -= self.moveDistance
                self.allowMove = False
            elif keyboard[pygame.K_d]:
                self.x += self.moveDistance
                self.allowMove = False
            elif keyboard[pygame.K_w]:
                self.y -= self.moveDistance
                self.allowMove = False
            elif keyboard[pygame.K_s]:
                self.y += self.moveDistance
                self.allowMove = False
        elif True not in keyboard:
            self.allowMove = True

    def draw(self):
        pygame.draw.rect(Window, (255, 255, 255), (self.x, self.y, 10, 10))

    def loop(self):
        self.detectkeyboard()


class Platform():
    def __init__(self, x: int, y: int) -> None:
        self.size: int = CELLSIZE
        self.x = x * self.size
        self.y = y * self.size

def Draw():
    global players
    localPlayers = players
    for player in localPlayers:
        player.draw()

pygame.init()

windowSize: tuple[int, int]
CELLSIZE: int
players: list[Player]

windowSize = (800, 600)
CELLSIZE = round((windowSize[1] - 100) / 20)
players = [Player(1, 1)]

print(CELLSIZE)
Window = pygame.display.set_mode(windowSize)
pygame.display.set_caption("Maze Simulator")

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit('Quit the game!')
            
    Window.fill((45, 12, 43))

    for player in players:
        player.loop()

    Draw()

    pygame.display.update()