file = open('day10.txt', 'r')
lines = file.readlines()

for i in range(0, len(lines)):
    lines[i] = lines[i].strip('\n')

scores = []
for line in lines:
    score = 0
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
                skip = 1
                break
            elif line[x] == outstack[-1]:
                del outstack[-1]
            else:
                skip = 1
                break
        elif line[x] == ']':
            if len(outstack) == 0:
                skip = 1
                break
            elif line[x] == outstack[-1]:
                del outstack[-1]
            else:
                skip = 1
                break
        elif line[x] == '>':
            if len(outstack) == 0:
                skip = 1
                break
            elif line[x] == outstack[-1]:
                del outstack[-1]
            else:
                skip = 1
                break
        elif line[x] == '}':
            if len(outstack) == 0:
                skip = 1
                break
            elif line[x] == outstack[-1]:
                del outstack[-1]
            else:
                skip = 1
                break
    if skip == 0:
        while len(outstack) >= 1:
            score = score * 5
            if outstack[-1] == ')':
                score += 1
                del outstack[-1]
            elif outstack[-1] == ']':
                score += 2
                del outstack[-1]
            elif outstack[-1] == '}':
                score += 3
                del outstack[-1]
            elif outstack[-1] == '>':
                score += 4
                del outstack[-1]
        scores.append(score)
scores.sort()
print(scores[len(scores)//2])
