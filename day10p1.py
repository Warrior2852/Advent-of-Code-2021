file = open('day10.txt', 'r')
lines = file.readlines()

for i in range(0, len(lines)):
    lines[i] = lines[i].strip('\n')

total = 0
for line in lines:
    outstack = []
    skip = 0
    for x in range(0, len(line)):
        if line[x] == '(':
            outstack.append(')')
        elif line[x] == '[':
            outstack.append(']')
        elif line[x] == '<':
            outstack.append('>')
        elif line[x] == '{':
            outstack.append('}')
        elif line[x] == ')':
            if len(outstack) == 0:
                total += 3
                break
            elif line[x] == outstack[-1]:
                del outstack[-1]
            else:
                total += 3
                break
        elif line[x] == ']':
            if len(outstack) == 0:
                total += 57
                break
            elif line[x] == outstack[-1]:
                del outstack[-1]
            else:
                total += 57
                break
        elif line[x] == '>':
            if len(outstack) == 0:
                total += 25137
                break
            elif line[x] == outstack[-1]:
                del outstack[-1]
            else:
                total += 25137
                break
        elif line[x] == '}':
            if len(outstack) == 0:
                total += 1197
                break
            elif line[x] == outstack[-1]:
                del outstack[-1]
            else:
                total += 1197
                break
print(total)
