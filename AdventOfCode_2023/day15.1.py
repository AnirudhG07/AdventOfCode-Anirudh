def hash_value(code):
    final=0
    for i in code:
        ascii=ord(i)
        final+=ascii
        final=final*17
        final=final%256
    return final

with open('./Ques_Practise/AdventOfCode_2023/day15.txt') as f:
    data = f.read().strip()
    hash_data=data.split(',')
    total_sum=0
    for i in hash_data:
        total_sum+=hash_value(i)
    print(total_sum)    