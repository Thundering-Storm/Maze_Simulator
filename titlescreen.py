import pygame
from rich import print

pygame.init()

windowSize = (800, 600)
clickedStart = False
optionsOpen = False
mouseX, mouseY = pygame.mouse.get_pos()
mousePressed = pygame.mouse.get_pressed()
mouseRect = pygame.Rect(mouseX, mouseY, 1, 1)


startbutton = pygame.Rect(windowSize[0] // 2 - 100, windowSize[1] / 2 - 50, 200, 100)

# optionsbutton = pygame.Rect()

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
    global clickedStart
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
            pygame.draw.rect(Window, (125, 255, 0), leaderboardbutton)
            Text(f'Play', windowSize[0] // 2 - 50, windowSize[1] / 2 - 25, (255, 255, 255))

        if collidebutton(startbutton, mouseRect, mousePressed):
            clickedStart = True

        pygame.display.update()

if __name__ == "__main__":
    start()