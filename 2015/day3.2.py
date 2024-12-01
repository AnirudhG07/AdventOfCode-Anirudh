def common_houses(dir):
    coordinates={(0,0)}
    position=(0,0)
    for char in dir:
        if char=='>':
            position=(position[0]+1,position[1])
            coordinates.add(position)
        elif char=='<':
            position=(position[0]-1,position[1])
            coordinates.add(position)
        elif char=='^':
            position=(position[0],position[1]+1)
            coordinates.add(position)
        elif char=='v':
            position=(position[0],position[1]-1)
            coordinates.add(position)
    
    return coordinates
    
def input_alternate_characters(input,x):
    alt_input=''
    for i in range(x, len(input), 2):
        alt_input+=input[i]
    return alt_input
with open("./Ques_Practise/AdventOfCode_2015/day3.txt", "r") as f:
    input=f.read()
    santa=input_alternate_characters((input),0)
    robo_santa=input_alternate_characters(input,1)
    net_houses=common_houses(santa).union(common_houses(robo_santa))
    print(len(net_houses),net_houses)