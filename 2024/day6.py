input = """
....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#...
"""
with open("./day6.txt", "r") as file:
    input = file.read()
data = [list(line.strip()) for line in input.strip().split('\n')]
# Find "^" in the data
x,y = 0,0
for col, row in enumerate(data):
    if '^' in row:
        y = row.index('^')
        x = col
        break
directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
current_direction = 0

walked = set()
walked.add((x, y))
data[x][y] = '.'

def can_move(x, y, dx, dy):
    new_x, new_y = x + dx, y + dy
    return 0 <= new_x < len(data) and 0 <= new_y < len(data[0]) and data[new_x][new_y] == '.'

while True:
    dx, dy = directions[current_direction]
    if can_move(x, y, dx, dy):
        x += dx
        y += dy
        walked.add((x, y))
    else:
        current_direction = (current_direction + 1) % 4
        dx, dy = directions[current_direction]
        if not can_move(x, y, dx, dy):
            break

print(len(walked))
