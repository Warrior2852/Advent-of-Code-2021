file = open('day6.txt', 'r')
lines = file.readlines()
fishlist = lines[0].split(',')
fishlist[-1] = fishlist[-1].strip('\n')
for a in range(0, len(fishlist)):
    fishlist[a] = int(fishlist[a])

for i in range(0, 80):
    newfishlist = []
    for x in range(0, len(fishlist)):
        if fishlist[x] == 0:
            newfishlist.append(6)
            newfishlist.append(8)
        else:
            newfishlist.append(fishlist[x]-1)
    fishlist = newfishlist

print(len(fishlist))
