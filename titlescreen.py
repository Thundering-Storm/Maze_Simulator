import pygame
from rich import print

pygame.init()

windowSize = (800, 600)
clickedStart = False
optionsOpen = False
mouseX, mouseY = pygame.mouse.get_pos()
mousePressed = pygame.mouse.get_pressed()
mouseRect = pygame.Rect(mouseX, mouseY, 1, 1)
diff = 0.3


startbutton = pygame.Rect(windowSize[0] // 2 - 100, windowSize[1] / 2 - 50, 200, 100)

optionsbutton = pygame.Rect(50, 50, 200, 100)

ezdiff = pygame.Rect(50, 300, 100, 50)

normaldiff = pygame.Rect(350, 300, 100, 50)

harddiff = pygame.Rect(650, 300, 100, 50)

leaveopt = pygame.Rect(50, 500, 250, 100)

leaderboardbutton = pygame.Rect(550, 50, 200, 100)

Window = pygame.display.set_mode(windowSize)
pygame.display.set_caption("Game")


def Text(string: str, x: float, y: float, color: tuple[int, int, int] = (255, 255, 255)) -> None:
    "Draws text on the screen"

    font = pygame.font.SysFont(None, 60)
    text = font.render(string, False, color)
    Window.blit(text, (x, y))

def collidebutton(otherRect: pygame.Rect, mouseRect: pygame.Rect, mousePressed):
    return mouseRect.colliderect(otherRect) and mousePressed[0]

def start() -> None:
    global clickedStart, optionsOpen, diff
    while not clickedStart:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit('Quit the game!')
        Window.fill((74, 12, 43))

        mouseX, mouseY = pygame.mouse.get_pos()
        mousePressed = pygame.mouse.get_pressed()
        mouseRect = pygame.Rect(mouseX, mouseY, 1, 1)

        if not optionsOpen:
            pygame.draw.rect(Window, (0, 255, 0), startbutton)
            pygame.draw.rect(Window, (100, 100, 100), optionsbutton)
            Text(f'Play', windowSize[0] // 2 - 50, windowSize[1] / 2 - 25, (255, 255, 255))
            Text('options', 75, 75, (255, 255, 255))
        
        if optionsOpen:
            pygame.draw.rect(Window, (0, 255, 0), ezdiff)
            pygame.draw.rect(Window, (225, 125, 0), normaldiff)
            pygame.draw.rect(Window, (255, 0, 0), harddiff)
            pygame.draw.rect(Window, (100, 100, 100), leaveopt)
            Text('eazy', 50, 300, (255, 255, 255))
            Text('nrml', 350, 300, (255, 255, 255))
            Text('hard', 650, 300, (255, 255, 255))
            Text('backToMenu', 50, 525, (255, 255, 255))

        if collidebutton(startbutton, mouseRect, mousePressed) and not optionsOpen:
            clickedStart = True

        if collidebutton(leaveopt, mouseRect, mousePressed) and optionsOpen:
            optionsOpen = False

        if collidebutton(ezdiff, mouseRect, mousePressed) and optionsOpen:
            diff = 0.1

        if collidebutton(normaldiff, mouseRect, mousePressed) and optionsOpen:
            diff = 0.3

        if collidebutton(harddiff, mouseRect, mousePressed) and optionsOpen:
            diff = 0.5

        if collidebutton(optionsbutton, mouseRect, mousePressed) and not optionsOpen:
            optionsOpen = True

        pygame.display.update()

def getdiff() -> float:
    return diff

if __name__ == "__main__":
    start()