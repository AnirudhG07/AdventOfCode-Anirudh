def colour_sum(colour:str):

    game=colour.split(':')[0].split(' ')[1]
    # print(game)
    colour=colour.split(':')[1].split(';')
    # print(colour)
    max_colour=[]
    for i in range(len(colour)):
        red,green,blue=0,0,0
        colour[i]=colour[i].split(',')
        # print(colour[i])
        
        for j in range(len(colour[i])):
            colour[i][j]=colour[i][j].split(',')
            # print(colour[i][j])
            colour[i][j][0]=colour[i][j][0].split(' ')
            # print(colour[i][j][0])
            if colour[i][j][0][2]=='red':
                if int(colour[i][j][0][1])>red:
                    red=(int(colour[i][j][0][1]))
            if colour[i][j][0][2]=='green':
                if int(colour[i][j][0][1])>green:
                    green=(int(colour[i][j][0][1]))
            if colour[i][j][0][2]=='blue':
                if int(colour[i][j][0][1])>blue:
                    blue=(int(colour[i][j][0][1]))
        max_colour.append((red,blue,green))
        # print(max_colour)
    return max(max_colour)
def max(colour):
    red,blue,green=0,0,0
    for i in range(len(colour)):
        if colour[i][0]>red:
            red=colour[i][0]
        if colour[i][1]>blue:
            blue=colour[i][1]
        if colour[i][2]>green:
            green=colour[i][2]
    return (red,blue,green)
            
with open("./Ques_Practise/AdventOfCode_2023/day2.txt", "r") as f:
    net_sum=0
    for line in f:
        colour_tupl = colour_sum(line.strip())
        prod=1
        for i in colour_tupl:
            prod*=i
        net_sum+=prod
    print(net_sum)