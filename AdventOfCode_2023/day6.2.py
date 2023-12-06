time=58819676
distance=434104122191218
initial=0
final=0
for i in range(0,time):
    if i*(time-i)>=distance:
        initial=i
        break
for i in range(time,0,-1):
    if i*(time-i)>=distance:
        final=i
        break
ways=final-initial+1
print(ways)