import random

def is_tile_empty(grid, x, y):
    if grid[x][y] == 0:
        return True
    else:
        return False

def is_grid_full(grid):
    for x in range(len(grid)):
        for y in range(len(grid[0])):
            if grid[x][y] == 0:
                return False

    return True

def gen_number():
    probability = random.randint(1, 10)
    value = 0

    if probability == 1:
        value = 4
    else:
        value = 2

    return value

def gen_new_tile(grid):
    if is_grid_full(grid):
        return

    x = random.randint(0, 3)
    y = random.randint(0, 3)

    while  not is_tile_empty(grid, x, y):
        x = random.randint(0, 3)
        y = random.randint(0, 3)

    grid[x][y] = gen_number()

def move(grid, direction):
    size = 4

    def move_line(line):
        new = [0] * size
        last = 0
        pos = 0

        for i in range(size):
            if line[i] != 0:
                if last == 0:
                    last = line[i]
                elif last == line[i]:
                    new[pos] = last * 2
                    pos += 1
                    last = 0
                else:
                    new[pos] = last
                    pos += 1
                    last = line[i]

        if last != 0:
            new[pos] = last

        return new

    if direction == 'a':  # left
        for i in range(size):
            grid[i] = move_line(grid[i])

    elif direction == 'd':  # right
        for i in range(size):
            grid[i] = move_line(grid[i][::-1])[::-1]

    elif direction == 'w':  # up
        for j in range(size):
            col = [grid[i][j] for i in range(size)]
            col = move_line(col)
            for i in range(size):
                grid[i][j] = col[i]

    elif direction == 's':  # down
        for j in range(size):
            col = [grid[i][j] for i in range(size)][::-1]
            col = move_line(col)[::-1]
            for i in range(size):
                grid[i][j] = col[i]

    return grid

def has_2048(grid):
    for row in grid:
        for value in row:
            if value == 2048:
                return True
    return False

def print_grid(grid):
    for row in grid:
        print(row)

def can_merge(grid):
    size = len(grid)

    for i in range(size):
        for j in range(size):
            current = grid[i][j]

            if current == 0:
                continue

            if j + 1 < size and grid[i][j + 1] == current:
                return True

            if i + 1 < size and grid[i + 1][j] == current:
                return True

    return False