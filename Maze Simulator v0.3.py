# Maze Simulator
import pygame
from sys import exit as quit
import maze

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
        global currentRoom
        new_x = self.gx + dx
        new_y = self.gy + dy

        # bounds check
        if new_y < 0 or new_y >= len(currentRoom):
            return
        if new_x < 0 or new_x >= len(currentRoom[0]):
            return

        # wall check
        if currentRoom[new_x][new_y] == 1:
            return

        self.gx = new_x
        self.gy = new_y

        if currentRoom[new_x][new_y] == 2:
            currentRoom, spawn = maze.generate_maze(25, 30)

            players = [Player(spawn[1], spawn[0])]

    def draw(self):
        px = SIDEBARLENGTH + self.gx * CELLSIZE + (CELLSIZE - self.size) // 2
        py = self.gy * CELLSIZE + (CELLSIZE - self.size) // 2

        pygame.draw.rect(Window, (255, 255, 255), (px, py, self.size, self.size))

    def loop(self) -> None:
        self.Movement()

def Draw() -> None:
    global players
    localPlayers = players # doing this has shown to improve performence

    Window.blit(sidebar, (0, 0))
    Window.blit(sidebarflip, (windowSize[0] - SIDEBARLENGTH, 0))

    for roomY in range(0, 30): # walls
        for roomX in range(0, 25):
            currentRoomIndex: int = currentRoom[roomX][roomY]
            if currentRoomIndex == 1:
                Window.blit(wall, (150 + roomX * 20, roomY * 20))
            elif currentRoomIndex == 2:
                pygame.draw.rect(Window, (0, 255, 0), (roomX * 20 + 150, roomY * 20, 20, 20))
            if currentRoomIndex == 3:
                pygame.draw.rect(Window, (0, 255, 255), (roomX * 20 + 150, roomY * 20, 20, 20))

    for player in localPlayers: # players
        player.draw()

def playerquit() -> None:
    quit('Quit the game!')

pygame.init()

windowSize: tuple[int, int]
CELLSIZE: int
players: list[Player]
SIDEBARLENGTH: int
level: int

sidebar = pygame.image.load('Assets/pictures/sidebar.png')
sidebarflip = pygame.transform.flip(sidebar, True, False)
wall = pygame.image.load('Assets/pictures/wall.png')
windowSize = (800, 600)
CELLSIZE = 20
SIDEBARLENGTH = int((windowSize[0] - (windowSize[1] - 100)) / 2)
level = 1
FPS = 120

currentRoom, spawn = maze.generate_maze(25, 30)

players = [Player(spawn[1], spawn[0])]

Window = pygame.display.set_mode(windowSize)
pygame.display.set_caption("Maze Simulator")
clock = pygame.time.Clock()

while True:
    time = clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            playerquit()
            
    Window.fill((255, 12, 43))

    for player in players:
        player.loop()

    Draw()

    pygame.display.update()