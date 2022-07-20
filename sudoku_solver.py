import copy

def line_to_grid(values):
    grid = []
    line = []
    for index, char in enumerate(values):
        if index and index % 9 == 0:
            grid.append(line)
            line = []
        line.append(int(char))
    grid.append(line)
    return grid

def grid_to_line(grid):
    line = ""
    for row in grid:
        r = "".join(str(x) for x in row)
        line += r
    return line

def small_square(x, y):
    upperX = ((x+3) // 3) * 3
    upperY = ((y+3) // 3) * 3
    lowerX = upperX - 3
    lowerY = upperY - 3
    for subX in range(lowerX, upperX):
        for subY in range(lowerY, upperY):
            if subX != x or subY != y:
                if not (subX == x and subY == y):
                    yield subX, subY

def compute_next_position(x, y):
    nextY = y
    nextX = (x + 1) % 9
    if nextX < x:
        nextY = (y + 1) % 9
        if nextY < y:
            return (True, 0, 0)
    return (False, nextX, nextY)

def test_and_remove(value, possible):
    if value != 0 and value in possible:
        possible.remove(value)

def detect_possible(grid, x, y):
    if grid[x][y]:
        return [grid[x][y]]
    possible = set(range(1, 10))
    for index in range(9):
        if index != y:
            test_and_remove(grid[x][index], possible)
        if index != x:
            test_and_remove(grid[index][y], possible)
    for subX, subY in small_square(x, y):
        test_and_remove(grid[subX][subY], possible)
    return list(possible)

def solve(start, x, y):
    temp = copy.deepcopy(start)
    while True:
        possible = detect_possible(temp, x, y)
        if not possible:
            return False
        finished, nextX, nextY = compute_next_position(x, y)
        if finished:
            temp[x][y] = possible[0]
            return temp
        if len(possible) > 1:
            break
        temp[x][y] = possible[0]
        x = nextX
        y = nextY
        for guess in possible:
            temp[x][y] = guess
            result = solve(temp, nextX, nextY)
            if result:
                return result
            return False
