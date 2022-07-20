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
