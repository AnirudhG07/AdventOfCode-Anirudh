def north_count(line):
    l=len(line)-1
    rocks=len([i for i in range(len(line)) if line[i]=='O'])
    print(rocks)
    for c in range(rocks):
        for i in range(l,0,-1):
            if line[i]=='O':
                line[i]='.'
                j=i-1
                while line[j]=='.' and j>-1:
                    j-=1
                line[j+1]='O'
    
    sum=0
    for i in range(len(line)):
        if line[i]=='O':
            sum+=(len(line)-i)
    return sum


with open('Ques_Practise/AdventOfCode_2023/day14.txt') as f:
    data=f.read().splitlines()
    column=[list(ele) for ele in zip(*data)]
    total_sum=0
    for col in column:
        total_sum+=north_count(col)
print(total_sum)
