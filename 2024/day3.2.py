import re

with open("day3.txt", "r") as f:
    data = f.read()

def extract_do_dont_mul(line):
    #define all the paterns
    mul_pattern = r"mul\(\s*(-?\d+)\s*,\s*(-?\d+)\s*\)"
    do_pattern = r"do\(\)"
    dont_pattern = r"don't\(\)"

    multiply = True
    sum = 0
    pos = 0
    while pos < len(line):
        # Check for do
        do_match = re.match(do_pattern, line[pos:])
        if do_match:
            multiply = True
            pos += do_match.end()
            continue

        dont_match = re.match(dont_pattern, line[pos:])
        if dont_match:
            multiply = False
            pos += dont_match.end()
            continue

        mul_match = re.match(mul_pattern, line[pos:])
        if mul_match:
            if multiply:
                x, y = int(mul_match.group(1)), int(mul_match.group(2))
                sum += x * y
            pos += mul_match.end()
            continue

        pos += 1

    return sum

print(extract_do_dont_mul(data))

# Regex inspired from some github repo
