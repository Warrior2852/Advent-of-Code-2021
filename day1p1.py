file = open('day1.txt', 'r')
lines = file.readlines()
prev = 0
count = -1
for i in lines:
    i.strip()
    i = int(i)
    if i > prev:
        count = count + 1
    prev = i
print(count)
        
