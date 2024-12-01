def ribbon(l,b,h):
    min_p=min(2*(l+b),2*(l+h),2*(b+h))
    return l*b*h+min_p
with open("./Ques_Practise/AdventOfCode_2015/day2.txt", "r") as f:
    net_sum=0
    for line in f:
        line=line.split("x")
        line_sum = ribbon(int(line[0]),int(line[1]),int(line[2]))
        net_sum+=line_sum
        print(line_sum)
    print(net_sum)
