def xyx_type(word):
    for i in range(len(word)-2):
        if word[i]==word[i+2]:
            return True
    return False
def qj_repeat_type(word):
    """
    It contains a pair of any two letters that appears at least twice in the string without overlapping,
    like xyxy (xy) or aabcdefgaa (aa), but not like aaa (aa, but it overlaps).
    >>> qj_repeat_type('qjhvhtzxzqqjkmpb')
    True
    >>> qj_repeat_type('xxyxx')
    True
    >>> qj_repeat_type('aaa')
    False
    """
    for i in range(len(word)-2):
        if word[i:i+2] in word[i+2:]:
            return True
    return False

def check(word):
    return xyx_type(word) and qj_repeat_type(word)
print(sum(check(line.strip()) for line in open('./Ques_Practise/AdventOfCode_2015/day5.txt')))