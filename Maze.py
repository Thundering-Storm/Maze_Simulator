import random

def generate_maze(width, height):
    maze = [[0 for _ in range(width)] for _ in range(height)]

    for y in range(height):
        for x in range(width):
            if random.random() < 0.3:
                maze[y][x] = 1

    spawn_x, spawn_y = random.randint(1, width-2), random.randint(1, height-2)
    win_x, win_y = random.randint(1, width-2), random.randint(1, height-2)

    while maze[spawn_y][spawn_x] == 1 or maze[win_y][win_x] == 1:
        spawn_x, spawn_y = random.randint(1, width-2), random.randint(1, height-2)
        win_x, win_y = random.randint(1, width-2), random.randint(1, height-2)

    maze[spawn_y][spawn_x] = 3
    maze[win_y][win_x] = 2

    maze_str = ""
    for row in maze:
        maze_str += ", ".join(map(str, row)) + ", "

    return maze_str.strip()
