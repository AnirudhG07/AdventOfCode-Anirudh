def check_line(series):
    for i in range(len(series)):
        if series[i]!=0:
            return False
    return True
def next_term(series):
    series=series.split(' ')
    print(series)
    for i in range (len(series)):
        series[i]=int(series[i])
    next_term=series[-1]
    next_series=[1]*len(series)
    while check_line(series)!=True:
        for i in range(len(series)-1):
            next_series[i]=series[i+1]-series[i]
        next_series.pop(len(next_series)-1)
        next_term+=next_series[-1]
        print(next_series)
        series=next_series
    return next_term
with open("./Ques_Practise/AdventOfCode_2023/day9.txt") as f:
    total=0
    for line in f:
        total+=next_term(line)
    print(total)
    