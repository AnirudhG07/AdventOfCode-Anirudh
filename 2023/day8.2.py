import re
map_re = re.compile(r"(\w{3}) = \((\w{3}), (\w{3})\)")

directions = None
maps = {}
with open("./Ques_Practise/AdventOfCode_2023/day8.txt", "r") as f:
    data = f.readlines()
    directions = data[0].rstrip()

    for i in range(2, len(data)):
        line = data[i]
        pos, left, right = map_re.match(line).groups()
        maps[pos] = (left, right)     
def traversal(posn, directions, maps):
    count=0
    while posn[2]!= 'Z':
        dir=directions[count % len(directions)]
        if dir=='L':
            posn=maps[posn][0]
        else:
            posn=maps[posn][1]
        count+=1
    return count
A_start=[]
for pos in maps:
    if pos[2]=='A':
        A_start.append((pos, traversal(pos, directions, maps)))
print(A_start)
# Find lcm of A_start[i][1] which are 16271, 24253, 13201, 14429, 18113, 22411 which comes out to be 11,188,774,513,823