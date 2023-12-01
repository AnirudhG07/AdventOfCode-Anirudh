import re

def sum_each_line(line):
    # Use regular expression to find calibration values
    sum=0
    matches = re.findall(r'one|two|three|four|five|six|seven|eight|nine|\d', line)
    
    # Convert spelled-out numbers to digits
    digit_values = {'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5',
                    'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'}
    
    if matches[0] in ['one','two','three','four','five','six','seven','eight','nine']:
        sum=int(digit_values[matches[0]])
    else:
        sum=int(matches[0])
    if matches[-1] in ['one','two','three','four','five','six','seven','eight','nine']:
        sum=sum*10+int(digit_values[matches[-1]])
    else:
        sum=sum*10+int(matches[-1])
    return sum
    

with open("./Ques_Practise/AdventOfCode_2023/data1-1.txt", "r") as f:
    net_sum=0
    for line in f:
        line_sum = sum_each_line(line.strip())
        net_sum+=line_sum
        print(line_sum)
    print(net_sum)
