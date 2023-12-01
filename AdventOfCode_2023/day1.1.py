def sum_each_line(line:str)->int:
    sum=0
    num=['0','1','2','3','4','5','6','7','8','9']
    for i in range(len(line)):
        if line[i] in num:
            sum=10*sum+int(line[i])
            break
    # find first integer from back of line and add it to sum
    for i in range(len(line)-1,-1,-1):
        if line[i] in num:
            sum=10*sum+int(line[i])
            break
    return sum

with open("./Ques_Practise/AdventOfCode_2023/data1-1.txt", "r") as f:
    net_sum=0
    for line in f:
        line_sum = sum_each_line(line.strip())
        net_sum+=line_sum
        # print(line_sum)
    print(net_sum)
