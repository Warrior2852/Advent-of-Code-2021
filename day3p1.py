file = open('day3.txt', 'r')
lines = file.readlines()
depth = 0
epsilon = ""
gamma = ""
for x in range(0, len(lines[0])-1):
    curzero = 0
    curone = 0
    for i in lines:
        split = list(i)
        del split[-1]
        if split[x] == '0':
            curzero += 1
        elif split[x] == '1':
            curone += 1
    if curone > curzero:
        gamma = gamma + '1'
        epsilon = epsilon + '0'
    else:
        gamma = gamma + '0'
        epsilon = epsilon + '1'
        
gamma = int(gamma, 2)
epsilon = int(epsilon, 2)
power = gamma * epsilon
print(power)
