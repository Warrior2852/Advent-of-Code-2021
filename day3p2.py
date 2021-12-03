import copy
file = open('day3.txt', 'r')
lines = file.readlines()
depth = 0
o2 = ""
co2 = ""
sublist1 = copy.deepcopy(lines)
sublist2 = copy.deepcopy(lines)
sublist1a = []
sublist2a = []
a = 0
b = 0
while len(sublist1) > 1:
    curzero = 0
    curone = 0
    for i in sublist1:
        split = list(i)
        del split[-1]
        if split[a] == '0':
            curzero += 1
        elif split[a] == '1':
            curone += 1
    if curone >= curzero:
        for x in range(0, len(sublist1)):
            split = list(sublist1[x])
            del split[-1]
            if split[a] == '1':
                sublist1a.append(sublist1[x])
    else:
        for x in range(0, len(sublist1)):
            split = list(sublist1[x])
            del split[-1]
            if split[a] == '0':
                sublist1a.append(sublist1[x])
    sublist1 = copy.deepcopy(sublist1a)
    sublist1a = []
    a += 1
o2 = sublist1[0]

while len(sublist2) > 1:
    curzero = 0
    curone = 0
    for j in sublist2:
        split = list(j)
        del split[-1]
        if split[b] == '0':
            curzero += 1
        elif split[b] == '1':
            curone += 1
    if curone >= curzero:
        for y in range(0, len(sublist2)):
            split = list(sublist2[y])
            del split[-1]
            if split[b] == '0':
                sublist2a.append(sublist2[y])
    else:
        for y in range(0, len(sublist2)):
            split = list(sublist2[y])
            del split[-1]
            if split[b] == '1':
                sublist2a.append(sublist2[y])
    sublist2 = copy.deepcopy(sublist2a)
    sublist2a = []
    b += 1
co2 = sublist2[0]
        
o2 = int(o2, 2)
co2 = int(co2, 2)
life = o2 * co2
print(life)
