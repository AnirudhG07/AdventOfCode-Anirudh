def wrapping(l,b,h):
    area_minside=min(l*b,l*h,b*h)
    return 2*(l*b+l*h+b*h)+area_minside

with open("./Ques_Practise/AdventOfCode_2015/day2.txt", "r") as f:
    net_sum=0
    for line in f:
        line=line.split("x")
        line_sum = wrapping(int(line[0]),int(line[1]),int(line[2]))
        net_sum+=line_sum
        print(line_sum)
    print(net_sum)