file = open('day7.txt', 'r')
lines = file.readlines()
crabs = lines[0].split(',')
crabs[-1] = crabs[-1].strip('\n')
for a in range(0, len(crabs)):
    crabs[a] = int(crabs[a])

currentfuel = 0
lowestfuel = 0
for i in crabs:
    currentfuel = 0
    complete = 1
    for j in crabs:
        if j < i:
            currentfuel += (i - j)
        if i < j:
            currentfuel += (j - i)
        if currentfuel > lowestfuel and lowestfuel != 0:
            complete = 0
            break
    if complete == 1:
        lowestfuel = currentfuel

print(lowestfuel)
