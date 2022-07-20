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
