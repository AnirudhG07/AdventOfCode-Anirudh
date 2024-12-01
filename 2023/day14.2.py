def north(line):
    l=len(line)-1
    rocks=len([i for i in range(len(line)) if line[i]=='O'])
    for c in range(rocks):
        for i in range(l,0,-1):
            if line[i]=='O':
                line[i]='.'
                j=i-1
                while j>-1 and line[j]=='.':
                    j-=1
                line[j+1]='O'
    return line
def south(line):
    l=len(line)-1
    rocks=len([i for i in range(len(line)) if line[i]=='O'])
    for c in range(rocks):
        for i in range(0,l,1):
            if line[i]=='O':
                line[i]='.'
                j=i+1
                while j<len(line) and line[j]=='.':
                    j+=1
                line[j-1]='O'
    return line

with open('Ques_Practise/AdventOfCode_2023/day14.txt') as f:
    data=f.read().splitlines()

def rotation(data):
    column=[list(ele) for ele in zip(*data)]
    collection=[]
    for col in column:
        collection.append(north(col))
    column=[list(ele) for ele in zip(*collection)]
    collection=[]
    for col in column:
        collection.append(north(col))
    column=[list(ele) for ele in zip(*collection)]
    collection=[]
    for col in column:
        collection.append(south(col))
    column=[list(ele) for ele in zip(*collection)]
    collection=[]
    for col in column:
        collection.append(south(col))
    return collection

for i in range(10**9):
    data=rotation(data)

def north_count(line):
    l=len(line)-1
    sum=0
    for i in range(len(line)):
        if line[i]=='O':
            sum+=(len(line)-i)
    return sum
total_sum=0
column=[j for j in zip(*data)]
for col in column:
    c=[i for i in col]
    total_sum+=north_count(c)
print(total_sum)