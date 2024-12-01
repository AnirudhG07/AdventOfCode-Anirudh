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

def box_part(hash_data):
    box = [[] for x in range(256)]

    for code in hash_data:
        if code[-1]=='-':
            name = code[:-1]
            val = hash_value(name)
            box[val] = [(i,j) for (i,j) in box[val] if i!=name]

        elif code[-2]=='=':
            name = code[:-2]
            val = hash_value(name)
            length = int(code[-1])
            if name in [i for (i,j) in box[val]]:
                box[val] = [(i, length if name==i else j) for (i,j) in box[val]]
            else:
                box[val].append((name, length))

    final_total=0
    for i1,boxes in enumerate(box):
        for i2,(i,j) in enumerate(boxes):
            final_total += j* (i1+1)*(i2+1)
    return final_total
print(box_part(hash_data))