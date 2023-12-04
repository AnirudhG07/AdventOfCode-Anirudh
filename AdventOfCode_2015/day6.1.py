def toggle_through(matrix,a,b,c,d):
    # swap 1 and 0 in the matrix in the square starting from (a,b) and ending at (c,d)
    for i in range(a, c+1):
        for j in range(b, d+1):
            if matrix[i][j]==1:
                matrix[i][j]=0
            else:
                matrix[i][j]=1
def turn_on(matrix,a,b,c,d):
    # put 1 in the matrix in the square starting from (a,b) and ending at (c,d)
    for i in range(a, c+1):
        for j in range(b, d+1):
            matrix[i][j] = 1
    
def turn_off(matrix,a,b,c,d):
    # put 0 in the matrix in the square starting from (a,b) and ending at (c,d)
    for i in range(a, c+1):
        for j in range(b, d+1):
            matrix[i][j] = 0

def instruction_decoder(line,matrix):
    if 'turn on' in line:
        line=line.split(',')
        line[0]=line[0].split(' ')
        line[1]=line[1].split(' ')
        d=int(line[2])
        a=int(line[0][2])
        b=int(line[1][0])
        c=int(line[1][2])
        turn_on(matrix,a,b,c,d)
    elif 'turn off' in line:
        line=line.split(',')
        line[0]=line[0].split(' ')
        line[1]=line[1].split(' ')
        d=int(line[2])
        a=int(line[0][2])
        b=int(line[1][0])
        c=int(line[1][2])
        turn_off(matrix,a,b,c,d)
    elif 'toggle' in line:
        line=line.split(',')
        line[0]=line[0].split(' ')
        line[1]=line[1].split(' ')
        d=int(line[2])
        a=int(line[0][1])
        b=int(line[1][0])
        c=int(line[1][2])
        toggle_through(matrix,a,b,c,d)

matrix=[[0 for i in range(1000)] for j in range(1000)]
with open('./Ques_Practise/AdventOfCode_2015/day6.txt') as f:
    for line in f:
        instruction_decoder(line,matrix)
on_lights=0
for i in range(1000):
    for j in range(1000):
        if matrix[i][j]==1:
            on_lights+=1
print(matrix)
print(on_lights)