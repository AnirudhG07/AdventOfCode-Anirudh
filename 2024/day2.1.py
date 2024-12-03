with open("./day2.txt", "r") as f:
    data = f.readlines()

def check_safe(line):
    # Check if all numbers in line are increasing or decreasing with 1 to 3 difference
    inc = True if int(line[0]) <= int(line[1]) else False

    if inc:
        for i in range(len(line) - 1):
            if not 1<= int(line[i+1]) - int(line[i]) <= 3:
                return False
    else:
        for i in range(len(line) - 1):
            if not 1<= int(line[i]) - int(line[i+1]) <= 3:
                return False

    return True

count = 0
for i in range(len(data)):
    flag = check_safe(data[i].split())
    if flag:
        count += 1

print(count)

