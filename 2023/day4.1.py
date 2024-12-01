import re
def score_card(card):
    card=card.split(':')
    card=card[1].split('|')

    card[0]=card[0].split(' ')
    card[1]=card[1].split(' ')
    print(card[0],card[1])

    winners = set()
    my_num = set()
    for item in card[0]:
        if item.isdigit():
            winners.add(int(item))
    for item in card[1]:
        if item.isdigit():
            my_num.add(int(item))

    won_num=set()
    for num in my_num:
        if num in winners:
            won_num.add(num)
    return 2**(len(won_num)-1) if len(won_num) > 0 else 0


with open("./Ques_Practise/AdventOfCode_2023/day4.txt", "r") as f:
    total_sum=0
    for line in f:
        line=line.strip()
        total_sum+=score_card(line)
print(total_sum)