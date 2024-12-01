with open("./Ques_Practise/AdventOfCode_2023/day11.txt") as f:
    data=f.read().splitlines()

empty_rows=[i for i,row in enumerate(data) if all(x =='.' for x in row)]
empty_column=[j for j,col in enumerate(zip(*data)) if all(x=='.' for x in col)]

# Finding all the coordinates with '#'
hash_coordinates=[]
for i in range(len(data)):
    for j in range(len(data[0])):
        if data[i][j]=='#':
            hash_coordinates.append((i,j)) 
net_sum, extra=0,2

for k,(i,j) in enumerate(hash_coordinates):
    for (m,n) in hash_coordinates[:k]:
        for row in range(min(i,m),max(i,m)):
            net_sum+=extra if row in empty_rows else 1
        for col in range(min(j,n),max(j,n)):
            net_sum+=extra if col in empty_column else 1
print(net_sum)