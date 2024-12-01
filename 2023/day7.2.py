from functools import cmp_to_key 
def frequency_string(hand):
    freq = {}
    for c in hand:
        if c in freq:
            freq[c] += 1
        else:
            freq[c] = 1
    if len(freq)==1:
        return 7
    elif len(freq)==2:
        if 'J' in hand:
            return 7
        else:
            if 1 in freq.values():
                return 6
            else:
                return 5
    elif len(freq)==3:
        if 3 in freq.values():
            if 'J' in hand:
                return 6
            else:
                return 4
        else:
            if 'J' in hand:
                if hand.count('J')==1:
                    return 5
                else:
                    return 6
            else:
                return 3
    elif len(freq)==4:
        if 'J' in hand:
            return 4
        else:
            return 2
    else: 
        if 'J' in hand:
            return 2
        else: return 1
print(frequency_string('KK777'))
def comparison(hand1, hand2):
    if frequency_string(hand1[0]) > frequency_string(hand2[0]):
        return True
    elif frequency_string(hand1[0]) == frequency_string(hand2[0]):
        basis=['A','K','Q','T','9','8','7','6','5','4','3','2','J']
        for i in range(5):
            if basis.index(hand1[0][i]) < basis.index(hand2[0][i]):  # hand1 > hand2
                return True
            elif basis.index(hand1[0][i]) == basis.index(hand2[0][i]):
                continue
            else:
                return False
    else:
        return False

with open('Ques_Practise/AdventOfCode_2023/day7.txt') as f:
    lines = f.readlines()
    hands_bid=[]
    for line in lines:
        hands_bid.append(line.split())
    # sort hands_bid[i][0] with comparison function
    for i in range(len(hands_bid)):
        for j in range(i+1, len(hands_bid)):
            if comparison(hands_bid[i], hands_bid[j]):
                hands_bid[i], hands_bid[j] = hands_bid[j], hands_bid[i]
    winning_sum=0
    for i in range(len(hands_bid)):
        winning_sum+=(i+1)*int(hands_bid[i][1])
    print(winning_sum)