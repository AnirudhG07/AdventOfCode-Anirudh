with open("./day1.txt", "r") as f:
    data = f.readlines()
    data = [x.split() for x in data]

col1 = [int(x[0]) for x in data]
col2 = [int(x[1]) for x in data]

col1.sort()
col2.sort()

sum = 0
for i in range(len(col1)):
    sum += abs(col1[i] - col2[i])

print(sum)
