# Maze Simulator
import pygame
from sys import exit as quit
import maze
import time

class Player():
    def __init__(self, x: int, y: int) -> None:
        self.size: int = 15
        center: float = (CELLSIZE - self.size) / 2
        self.gx: int = x
        self.gy: int = y
        self.moveDistance: float = CELLSIZE
        self.allowMove: bool = True
    
    def Movement(self) -> None:
        "Checks wasd to move the player"
        keyboard = pygame.key.get_pressed()
        if self.allowMove:
            if keyboard[pygame.K_a]:
                self.move(-1, 0)
                self.allowMove = False
            if keyboard[pygame.K_d]:
                self.move(1, 0)
                self.allowMove = False
            if keyboard[pygame.K_w]:
                self.move(0, -1)
                self.allowMove = False
            if keyboard[pygame.K_s]:
                self.move(0, 1)
                self.allowMove = False
            if keyboard[pygame.K_ESCAPE]:
                playerquit()
        elif True not in keyboard:
            self.allowMove = True

    def move(self, dx: int, dy: int) -> None:
        "Moves the player"
        global currentRoom, wincounter
        newX = self.gx + dx
        newY = self.gy + dy

        # bounds check
        if newY < 0 or newY >= len(currentRoom) + 5:
            return
        if newX < 0 or newX >= len(currentRoom[0]):
            return

        # wall check
        if currentRoom[newX][newY] == 1:
            return

        move.play()
        self.gx = newX
        self.gy = newY

        if currentRoom[newX][newY] == 2:
            currentRoom, spawn = maze.generateMaze(25, 30)
            win.play()
            wincounter += 1
            self.gx = spawn[1]
            self.gy = spawn[0]

    def draw(self) -> None:
        "draws the player"
        px = SIDEBARLENGTH + self.gx * CELLSIZE + (CELLSIZE - self.size) // 2
        py = self.gy * CELLSIZE + (CELLSIZE - self.size) // 2

        pygame.draw.rect(Window, (255, 255, 255), (px, py, self.size, self.size))

    def loop(self) -> None:
        "Game loop for the player"
        self.Movement()

def Draw() -> None:
    "Draws stuff"
    global players

    Window.blit(sidebar, (0, 0))
    Window.blit(sidebarflip, (windowSize[0] - SIDEBARLENGTH, 0))

    for roomY in range(0, 30): # walls
        for roomX in range(0, 25):
            currentRoomIndex: int = currentRoom[roomX][roomY]
            if currentRoomIndex == 1:
                Window.blit(wall, (150 + roomX * 20, roomY * 20))
            elif currentRoomIndex == 2:
                Window.blit(winblock, (150 + roomX * 20, roomY * 20))

    player.draw()

    Text(f'{wincounter}', 65, 50, (255, 255, 255))

def Text(string: str, x: float, y: float, color: tuple[int, int, int] = (255, 255, 255)) -> None:
    "Draws text on the screen"

    font = pygame.font.SysFont(None, 60)
    text = font.render(string, False, color)
    Window.blit(text, (x, y))

def playerquit() -> None:
    year = time.localtime().tm_year
    yday = time.localtime().tm_yday
    currentTime = f'date={year}, {yday}'
    with open("Assets/highscore.txt", "a") as savefile:
        savefile.write(f'{wincounter=}, {currentTime=}\n')
    print(f'{wincounter=}, {currentTime=}')

    
    
    quit('Quit the game!')

pygame.init()
pygame.mixer.init()

# type definitions (got lazy so not all variables are here)
windowSize: tuple[int, int]
CELLSIZE: int
players: list[Player]
SIDEBARLENGTH: int
level: int

# variables
sidebar = pygame.image.load('Assets/pictures/sidebar.png')
sidebarflip = pygame.transform.flip(sidebar, True, False)
wall = pygame.image.load('Assets/pictures/wall.png')
move = pygame.mixer.Sound('Assets/sounds/move.wav')
win = pygame.mixer.Sound('Assets/sounds/win.wav')
winblock = pygame.image.load('Assets/pictures/winblock.png')
windowSize = (800, 600)
CELLSIZE = 20
SIDEBARLENGTH = int((windowSize[0] - (windowSize[1] - 100)) / 2)
level = 1
FPS = 120
wincounter = 0

currentRoom, spawn = maze.generateMaze(25, 30)

player = Player(spawn[1], spawn[0])
# idk why i have to do 1, 0 and not 0, 1 but ok if it works it works

Window = pygame.display.set_mode(windowSize)
pygame.display.set_caption("Maze Simulator")
clock = pygame.time.Clock()

while True:
    dt = clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            playerquit()
            
    Window.fill((22, 14, 255))

    player.loop()

    Draw()

    pygame.display.update()