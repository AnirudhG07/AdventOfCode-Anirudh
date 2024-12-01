with open("./Ques_Practise/AdventOfCode_2023/day13.txt") as f:
    matrix = f.read().strip()
    patterns = [[i for i in row] for row in matrix.split("\n")]

ans = 0
for grid in matrix.split('\n\n'):
    patterns = [[c for c in row] for row in grid.split('\n')]
    row= len(patterns)
    cols = len(patterns[0])

    for c in range(cols-1):
        bugs = 0
        for i in range(cols):
            left = c-i
            right = c+1+i
            if 0<= left<right<cols:
                for r in range(row):
                    if patterns[r][left] != patterns[r][right]:
                        bugs+=1
        if bugs == 1:
            ans += c+1

    for r in range(row-1):
        bugs = 0
        for j in range(row):
            up = r-j
            down = r+1+j
            if 0<= up < down < row:
                for c in range(cols):
                    if patterns[up][c] != patterns[down][c]:
                        bugs += 1
        if bugs == 1:
            ans += 100*(r+1)
print(ans)