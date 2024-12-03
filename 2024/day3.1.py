with open("day3.txt", "r") as f:
    data = f.read() 
    
import re

nums = []
pattern = r"mul\(\d+,\d+\)"
for match in re.findall(pattern, data):
    nums.append([int(x) for x in re.findall(r"\d+", match)])

print(sum([x[0] * x[1] for x in nums]))
