def present(posn, coordinates):
    if posn in coordinates:
        return True
    return False
def common_houses(dir):
    coordinates={(0,0):1}
    position=(0,0)
    for i in range(len(dir)):
        if dir[i]=='>':
            position=(position[0]+1,position[1])
            if not present(position,coordinates):
                coordinates[position]=1
            else:
                coordinates[position]+=1
        elif dir[i]=='<':
            position=(position[0]-1,position[1])
            if not present(position,coordinates):
                coordinates[position]=1
            else:
                coordinates[position]+=1
        elif dir[i]=='^':
            position=(position[0],position[1]+1)
            if not present(position,coordinates):
                coordinates[position]=1
            else:
                coordinates[position]+=1
        elif dir[i]=='v':
            position=(position[0],position[1]-1)
            if not present(position,coordinates):
                coordinates[position]=1
            else:
                coordinates[position]+=1
    print(coordinates)

    cmn_houses=0
    for cord in coordinates:
        if coordinates[cord]>=1:
            cmn_houses+=1
    return cmn_houses

with open("./Ques_Practise/AdventOfCode_2015/day3.txt", "r") as f:
    
    print(common_houses(f.read()))