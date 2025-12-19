import random

def generate_maze(height, width):
    maze = [[0 for _ in range(height)] for _ in range(width)]

    for y in range(width):
        for x in range(height):
            if random.random() < 0.3:
                maze[y][x] = 1

    spawn_x, spawn_y = random.randint(1, height-2), random.randint(1, width-2)
    win_x, win_y = random.randint(1, height-2), random.randint(1, width-2)

    while maze[spawn_y][spawn_x] == 1 or maze[win_y][win_x] == 1:
        spawn_x, spawn_y = random.randint(1, height-2), random.randint(1, width-2)
        win_x, win_y = random.randint(1, height-2), random.randint(1, width-2)

    maze[spawn_y][spawn_x] = 3
    maze[win_y][win_x] = 2

    return maze
