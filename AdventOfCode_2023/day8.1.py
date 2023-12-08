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
print(maps)
def traversal(directions, maps):
    posn='AAA'
    count=0
    while posn != 'ZZZ':
        dir=directions[count % len(directions)]
        if dir=='L':
            posn=maps[posn][0]
        else:
            posn=maps[posn][1]
        count+=1
    return count

count = traversal(directions, maps)
print(count)
