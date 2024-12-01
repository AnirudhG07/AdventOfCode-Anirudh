import re
def card_wins(card):
    card=card.split(':')
    card=card[1].split('|')

    card[0]=card[0].split(' ')
    card[1]=card[1].split(' ')
    # print(card[0],card[1])

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
    return len(won_num)

with open("./Ques_Practise/AdventOfCode_2023/day4.txt", "r") as f:
    card_count=[]
    for card_num,line in enumerate(f):
        line=line.strip()
        card_count.append((card_num+1,card_wins(line),1))

def recursive_card_count(card_count):
    recur_count=[1]*len(card_count)
    for n in range(len(card_count)):
        for i in range(card_count[n][1]):
            recur_count[n+1+i]+=recur_count[n]
    print(recur_count)
    return sum(recur_count)
print(recursive_card_count(card_count))
