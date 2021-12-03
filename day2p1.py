file = open('day2.txt', 'r')
lines = file.readlines()
current = []
depth = 0
horizon = 0
for i in lines:
    i.strip()
    current = i.split()
    if current[0] == "forward":
        horizon += int(current[1])
    elif current[0] == "down":
        depth += int(current[1])
    elif current[0] == "up":
        depth -= int(current[1])
total = horizon * depth
print(total)
