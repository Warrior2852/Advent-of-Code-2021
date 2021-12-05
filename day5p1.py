def newoverlapcheck(covered, coords, overlaps):
    count = 0
    for i in range(0, len(covered)):
        if covered[i] == coords:
            count += 1
    if count == 1:
        return overlaps + 1
    else:
        return overlaps

file = open('day5.txt', 'r')
lines = file.readlines()

for a in range(0, len(lines)):
    lines[a] = lines[a].strip('\n')
covered = []
overlaps = 0
coords = []
for i in lines:
    row = i.split(" -> ")
    first = row[0].split(',')
    second = row[1].split(',')
    first[0] = int(first[0])
    first[1] = int(first[1])
    second[0] = int(second[0])
    second[1] = int(second[1])
    if first[0] == second[0]:
        if first[1] >= second[1]:
            for i in range(0, ((first[1]-second[1]) + 1)):
                coords = [second[0], (second[1] + i)]
                overlaps = newoverlapcheck(covered, coords, overlaps)
                covered.append(coords)
        if first[1] < second[1]:
            for i in range(0, ((second[1]-first[1]) + 1)):
                coords = [first[0], (first[1] + i)]
                overlaps = newoverlapcheck(covered, coords, overlaps)
                covered.append(coords)
    elif first[1] == second[1]:
        if first[0] >= second[0]:
            for i in range(0, ((first[0]-second[0]) + 1)):
                coords = [second[0] + i, (second[1])]
                overlaps = newoverlapcheck(covered, coords, overlaps)
                covered.append(coords)
        if first[0] < second[0]:
            for i in range(0, ((second[0]-first[0]) + 1)):
                coords = [first[0] + i, (first[1])]
                overlaps = newoverlapcheck(covered, coords, overlaps)
                covered.append(coords)
                
print(overlaps)
