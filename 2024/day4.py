with open("./day4.txt", "r") as f:
    data = f.readlines()

# Ceres search for "XMAS" in the data
data = [line.strip() for line in data]

# Convert data to a 2D grid
data = [list(line) for line in data]

dir_1 = [(1, 0), (0, 1), (-1, 0), (0, -1)]
diagonals = [(1, 1), (-1, -1), (1, -1), (-1, 1)]
def search_dir(grid, dx, dy, x, y, series):
    # Search for series in given direction starting from x, y
    for i in range(1, len(series)):
        nx, ny = x + i*dx, y + i*dy
        if nx < 0 or ny < 0 or nx >= len(grid[0]) or ny >= len(grid):
            return False
        if grid[ny][nx] != series[i]:
            return False
    return True

def part_1(grid, series):
    found = 0
    directions = dir_1 + diagonals
    for dir in directions:
        dx, dy = dir

        for y in range(len(grid)):
            for x in range(len(grid[y])):
                if grid[y][x] == series[0]:
                    if search_dir(grid, dx, dy, x, y, series):
                        found += 1

    return found

def search_around_A(grid, x, y):
    corners = [(x+1, y+1), (x+1, y-1), (x-1, y-1), (x-1, y+1)]
    data_corners = []
    for nx, ny in corners:
        if nx >= 0 and ny >= 0 and nx < len(grid[0]) and ny < len(grid):
            data_corners.append(grid[ny][nx] if grid[ny][nx] in ["M", "S"] else ".")
        else:
            data_corners.append(".")
    
    if data_corners.count("M") == 2 and data_corners.count("S") == 2:
        if "".join(data_corners) not in ["MSMS", "SMSM"]:
            return True
    return False

def part_2(grid):
    found = 0
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            if grid[y][x] == "A":
                if search_around_A(grid, x, y):
                    found += 1
                    print(x, y)
    return found
    

print("Part 1:", part_1(data, "XMAS"))
print("Part 2:", part_2(data))


