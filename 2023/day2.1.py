def check(colour_list):
    red,green, blue=12,13,14
    if colour_list[2]=='red':
        if int(colour_list[1])>red:
            return False
    if colour_list[2]=='green':
        if int(colour_list[1])>green:
            return False
    if colour_list[2]=='blue':
        if int(colour_list[1])>blue:
            return False
    return True

def colour_sum(colour:str):
    game=colour.split(':')[0].split(' ')[1]
    # print(game)
    colour=colour.split(':')[1].split(';')
    # print(colour)
    flag=True
    for i in range(len(colour)):
        colour[i]=colour[i].split(',')
        # print(colour[i])
        
        for j in range(len(colour[i])):
            colour[i][j]=colour[i][j].split(',')
            # print(colour[i][j])
            colour[i][j][0]=colour[i][j][0].split(' ')
            # print(colour[i][j][0])
            if not check(colour[i][j][0]):
                flag=False
                break
    if flag:
        return game
    else:
        return 0
with open("./Ques_Practise/AdventOfCode_2023/day2.txt", "r") as f:
    net_sum=0
    for line in f:
        line_sum = colour_sum(line.strip())
        net_sum+=int(line_sum)
        # print(line_sum)
    print(net_sum)