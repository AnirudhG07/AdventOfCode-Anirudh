with open("./day1.txt", "r") as f:
    data = f.readlines()
    data = [x.split() for x in data]

col1 = [int(x[0]) for x in data]
col2 = [int(x[1]) for x in data]

# for each element in col1, find its occurence in col2
freq = 0
for i in col1:
    freq += i*col2.count(i)

print(freq)
