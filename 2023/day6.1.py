time_distance=[(58,434),(81,1041),(96,2219),(76,1218)]
def race_win(time_distance):
    ways=[]
    for pair in time_distance:
        way=0
        dist=0
        for dist in range(pair[1]):
            if dist*(pair[0]-dist)>=pair[1]:
                way+=1
        ways.append(way)
    return ways
ways=race_win(time_distance)
prod=1
for i in ways:
    prod*=i
print(prod)