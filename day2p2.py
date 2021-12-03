file = open('day2.txt', 'r')
lines = file.readlines()
current = []
depth = 0
horizon = 0
aim = 0
for i in lines:
    i.strip()
    current = i.split()
    if current[0] == "forward":
        horizon += int(current[1])
        depth += aim * int(current[1])
    elif current[0] == "down":
        aim += int(current[1])
    elif current[0] == "up":
        aim -= int(current[1])
total = horizon * depth
print(total)
