def seeds_to_soil(seed_to_soil,seeds):
    arr=[0]*(10**10)
    for tuple in seed_to_soil:
        j=0
        for i in range(tuple[0],tuple[0]+tuple[2]):
            arr[tuple[1]+j]=i
            j+=1
    for i in range(len(arr)):
        if arr[i]==0:
            arr[i]=i
    l=[]
    for i in seeds:
        l.append(arr[i])
    return l
def soils_to_fertilizer(soil_to_fertilizer,seeds):
    arr=[0]*(10**10)
    for tuple in soil_to_fertilizer:
        j=0
        for i in range(tuple[0],tuple[0]+tuple[2]):
            arr[tuple[1]+j]=i
            j+=1
    for i in range(len(arr)):
        if arr[i]==0:
            arr[i]=i
    l=[]
    for i in seeds:
        l.append(arr[i])
    return l
def fertilizers_to_water(fertilizer_to_water,seeds):
    arr=[0]*(10**10)
    for tuple in fertilizer_to_water:
        j=0
        for i in range(tuple[0],tuple[0]+tuple[2]):
            arr[tuple[1]+j]=i
            j+=1
    for i in range(len(arr)):
        if arr[i]==0:
            arr[i]=i
    l=[]
    for i in seeds:
        l.append(arr[i])
    return l
    
def waters_to_light(water_to_light,seeds):
    arr=[0]*(10**10)
    for tuple in water_to_light:
        j=0
        for i in range(tuple[0],tuple[0]+tuple[2]):
            arr[tuple[1]+j]=i
            j+=1
    for i in range(len(arr)):
        if arr[i]==0:
            arr[i]=i
    l=[]
    for i in seeds:
        l.append(arr[i])
    return l
def lights_to_temperature(light_to_temperature,seeds):
    arr=[0]*(10**10)
    for tuple in light_to_temperature:
        j=0
        for i in range(tuple[0],tuple[0]+tuple[2]):
            arr[tuple[1]+j]=i
            j+=1
    for i in range(len(arr)):
        if arr[i]==0:
            arr[i]=i
    l=[]
    for i in seeds:
        l.append(arr[i])
    return l

def temperatures_to_humidity(temperature_to_humidity,seeds):
    arr=[0]*(10**10)
    for tuple in temperature_to_humidity:
        j=0
        for i in range(tuple[0],tuple[0]+tuple[2]):
            arr[tuple[1]+j]=i
            j+=1
    for i in range(len(arr)):
        if arr[i]==0:
            arr[i]=i
    l=[]
    for i in seeds:
        l.append(arr[i])
    return l
def humiditys_to_location(humidity_to_location,seeds):
    arr=[0]*(10**10)
    for tuple in humidity_to_location:
        j=0
        for i in range(tuple[0],tuple[0]+tuple[2]):
            arr[tuple[1]+j]=i
            j+=1
    for i in range(len(arr)):
        if arr[i]==0:
            arr[i]=i
    l=[]
    for i in seeds:
        l.append(arr[i])
    return l

def input_decoder(input):
    seeds=[]
    input[0]=input[0].split(':')[1]
    input[0]=input[0].split(' ')
    for i in range(1,len(input[0])):
        seeds.append(int(input[0][i]))

    seed_to_soil=[]
    soil_to_fertilizer=[]
    fertilizer_to_water=[]
    water_to_light=[]
    light_to_temperature=[]
    temperature_to_humidity=[]
    humidity_to_location=[]
    pt=3
    for i in range(pt,len(input)):
        if input[i]!='soil-to-fertilizer map:' and input[i]!='':
            seed_to_soil.append((int(input[i].split(' ')[0]),int(input[i].split(' ')[1]),int(input[i].split(' ')[2])))
        else:
            pt=i+2
            break
    for i in range(pt,len(input)):
        if input[i]!='fertilizer-to-water map:' and input[i]!='':
            soil_to_fertilizer.append((int(input[i].split(' ')[0]),int(input[i].split(' ')[1]),int(input[i].split(' ')[2])))
        else:
            pt=i+2
            break
    for i in range(pt,len(input)):
        if input[i]!='water-to-light map:' and input[i]!='':
            fertilizer_to_water.append((int(input[i].split(' ')[0]),int(input[i].split(' ')[1]),int(input[i].split(' ')[2])))
        else:
            pt=i+2
            break
    for i in range(pt,len(input)):
        if input[i]!='light-to-temperature map:' and input[i]!='':
            water_to_light.append((int(input[i].split(' ')[0]),int(input[i].split(' ')[1]),int(input[i].split(' ')[2])))
        else:
            pt=i+2
            break
    for i in range(pt,len(input)):
        if input[i]!='temperature-to-humidity map:' and input[i]!='':
            light_to_temperature.append((int(input[i].split(' ')[0]),int(input[i].split(' ')[1]),int(input[i].split(' ')[2])))
        else:
            pt=i+2
            break
    for i in range(pt,len(input)):
        if input[i]!='humidity-to-location map:' and input[i]!='':
            temperature_to_humidity.append((int(input[i].split(' ')[0]),int(input[i].split(' ')[1]),int(input[i].split(' ')[2])))
        else:
            pt=i+2
            break
    for i in range(pt,len(input)):
        humidity_to_location.append((int(input[i].split(' ')[0]),int(input[i].split(' ')[1]),int(input[i].split(' ')[2])))
    
    # print(seeds)
    # print(seed_to_soil)
    # print(soil_to_fertilizer)
    # print(fertilizer_to_water)
    # print(water_to_light)
    # print(light_to_temperature)
    # print(temperature_to_humidity)
    # print(humidity_to_location)

    arr=seeds_to_soil(seed_to_soil,seeds)
    arr=soils_to_fertilizer(soil_to_fertilizer,arr)
    arr=fertilizers_to_water(fertilizer_to_water,arr)
    arr=waters_to_light(water_to_light,arr)
    arr=lights_to_temperature(light_to_temperature,arr)
    arr=temperatures_to_humidity(temperature_to_humidity,arr)
    arr=humiditys_to_location(humidity_to_location,arr)
    print(min(arr))
    return 0

with open('./Ques_Practise/AdventOfCode_2023/day5.txt') as f:
    input=f.read()
    input=input.split('\n')
    input_decoder(input)


