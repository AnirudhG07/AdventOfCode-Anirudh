def nice_naught(word):
    vowels=['a','e','i','o','u']
    double_alphabet=['aa','bb','cc','dd','ee','ff','gg','hh','ii','jj','kk','ll','mm','nn','oo','pp','qq','rr','ss','tt','uu','vv','ww','xx','yy','zz']
    bad_alphabet=['ab','cd','pq','xy']
    for i in bad_alphabet:
        if i in word:
            return False
    double_alphabet_count=0
    for i in double_alphabet:
        if i in word:
            double_alphabet_count+=1
            break
    if double_alphabet_count<1:
        return False
    vowel_count=0
    for i in word:
        if i in vowels:
            vowel_count+=1
    if vowel_count<3:
        return False
    return True

with open('./Ques_Practise/AdventOfCode_2015/day5.txt') as f:
    count=0
    for line in f:
        if nice_naught(line.strip()):
            count+=1
    print(count)      