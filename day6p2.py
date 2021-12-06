file = open('day6.txt', 'r')
lines = file.readlines()
fishlist = lines[0].split(',')
fishlist[-1] = fishlist[-1].strip('\n')
for a in range(0, len(fishlist)):
    fishlist[a] = int(fishlist[a])

statuscheck = []
for b in range(0, 9):
    statuscheck.append(0)

for c in range(0, len(fishlist)):
    statuscheck[fishlist[c]] += 1

for i in range(0, 256):
    numtorepro = statuscheck[0]
    for x in range(0, 8):
        statuscheck[x] = statuscheck[x+1]
    statuscheck[6] += numtorepro
    statuscheck[8] = numtorepro

total = 0
for y in range(0, 9):
    total += statuscheck[y]

print(total)
