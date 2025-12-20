import random
import pygame
import titlescreen

currentdiff = 0.3

def setdiff(diff):
    global currentdiff
    currentdiff = diff

def generateMaze(height, width) -> tuple[list[list[int]], list[int]]:
    'Generates a maze'
    maze = [[0 for _ in range(width)] for _ in range(height)]
    mazeDetection = []

    for y in range(height):
        for x in range(width):
            if random.random() < currentdiff:
                maze[y][x] = 1

    spawnX = random.randint(1, width - 2)
    spawnY = random.randint(1, height - 2)
    winX = random.randint(1, width - 2)
    winY = random.randint(1, height - 2)

    while maze[spawnY][spawnX] == 1 or maze[winY][winX] == 1:
        spawnX = random.randint(1, width - 2)
        spawnY = random.randint(1, height - 2)
        winX = random.randint(1, width - 2)
        winY = random.randint(1, height - 2)

    maze[spawnY][spawnX] = 3
    maze[winY][winX] = 2

    spawn = [spawnX, spawnY]

    return maze, spawn