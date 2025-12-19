# Maze Simulator
import pygame
from sys import exit as quit
import maze

class Player():
    def __init__(self, x: int, y: int) -> None:
        self.size: int = 15
        center: float = (CELLSIZE - self.size) / 2
        self.x: float = x * CELLSIZE + SIDEBARLENGTH + center
        self.y: float = y * CELLSIZE + center
        self.moveDistance: float = CELLSIZE
        self.allowMove: bool = True
    
    def Movement(self) -> None:
        "Checks wasd to move the player"
        keyboard = pygame.key.get_pressed()
        if self.allowMove:
            if keyboard[pygame.K_a]:
                self.move('horisontal', '-')
                self.allowMove = False
            if keyboard[pygame.K_d]:
                self.move('horisontal', '+')
                self.allowMove = False
            if keyboard[pygame.K_w]:
                self.move('vertical', '-')
                self.allowMove = False
            if keyboard[pygame.K_s]:
                self.move('vertical', '+')
                self.allowMove = False
        elif True not in keyboard:
            self.allowMove = True

    def move(self, side: str, sign: str) -> None: 
        if side == 'horisontal':
            exec(f'self.x {sign}= self.moveDistance')
            # this probably isn't the best way to do this, but i dont care
        if side == 'vertical':
            exec(f'self.y {sign}= self.moveDistance')

    def draw(self) -> None:
        pygame.draw.rect(Window, (255, 255, 255), (self.x, self.y, self.size, self.size))

    def loop(self) -> None:
        self.Movement()

def Draw() -> None:
    global players
    localPlayers = players # doing this has shown to improve performence

    Window.blit(sidebar, (0, 0))
    Window.blit(sidebarflip, (windowSize[0] - SIDEBARLENGTH, 0))

    for player in localPlayers:
        player.draw()

    for roomY in range(0, 30):
        for roomX in range(0, 25):
            currentRoomIndex: int = currentRoom[roomX][roomY]  # 2D list indexing
            if currentRoomIndex == 1:
                Window.blit(wall, (150 + roomX * 20, roomY * 20))
            elif currentRoomIndex == 2:
                pygame.draw.rect(Window, (0, 255, 0), (roomX * 20 + 150, roomY * 20, 20, 20))
            elif currentRoomIndex == 3:
                pygame.draw.rect(Window, (0, 0, 255), (roomX * 20 + 150, roomY * 20, 20, 20))  # optional: show spawn



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

players = [Player(0, 0)]

currentRoom = maze.generate_maze(30, 25)

Window = pygame.display.set_mode(windowSize)
pygame.display.set_caption("Maze Simulator")

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit('Quit the game!')
            
    Window.fill((255, 12, 43))

    for player in players:
        player.loop()

    Draw()

    pygame.display.update()