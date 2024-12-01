import sys
import re
from collections import defaultdict


def sum_gears(input):
    lines = input.split('\n')

    matrix = [[col for col in line] for line in lines]

    length_m= len(matrix)
    length_line= len(matrix[0])

    left_out_num = 0
    nums = defaultdict(list)

    for r in range(len(matrix)):

        gears = set() # positions of '*' characters next to the current number
        n = 0
        has_part = False
        for col in range(len(matrix[r])+1):

            if col<length_line and matrix[r][col].isdigit():
                n = n*10+int(matrix[r][col])

                for row_num in [-1,0,1]:
                    for col_num in [-1,0,1]:    
                        if 0<=col+col_num<length_line and 0<=r+row_num<length_m :
                            char = matrix[r+row_num][col+col_num]

                            if not char.isdigit() and char != '.':
                                has_part = True
                            if char=='*':
                                gears.add((r+row_num, col+col_num))

            elif n>0:
                for gear in gears:
                    nums[gear].append(n)

                if has_part:
                    left_out_num += n
                n = 0

                has_part = False
                gears = set()
    sum_g = 0

    for c,var in nums.items():
        if len(var)==2:
            sum_g += var[0]*var[1]

    return sum_g

input= open("./Ques_Practise/AdventOfCode_2023/day3.txt").read()
input=input.strip()

print(sum_gears(input))

