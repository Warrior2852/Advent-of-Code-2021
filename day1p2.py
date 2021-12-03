file = open('day1.txt', 'r')
lines = file.readlines()
prev = 0
count = -1
for i in range(0, len(lines)-2):
    line1 = lines[i].strip()
    line1 = int(line1)
    line2 = lines[i+1].strip()
    line2 = int(line2)
    line3 = lines[i+2].strip()
    line3 = int(line3)
    total = line1 + line2 + line3
    #print(line1, line2, line3)
    if total > prev:
        count = count + 1
    prev = total
print(count)
        
