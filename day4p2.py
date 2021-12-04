def finder(board, check):
    present = 0
    coords = [0, 0]
    for i in range(0, len(board)):
        for x in range(0, len(board)):
            if int(board[i][x]) == int(check):
                present = 1
                coords = [i, x]
                return present, coords
    return present, coords

def donecheck(done):
    check = 0
    for i in range(0, len(done[0])):
        if int(done[0][i]) == 5:
            check = 1
            return check
    for j in range(0, len(done[1])):
        if int(done[1][j]) == 5:
            check = 1
            return check
    return check

def endcalc(board, ignore, last):
    addtotal = 0
    for i in range(0, len(board)):
        for j in range(0, len(board)):
            do = 1
            for x in range(0, len(ignore)):
                if int(i) == int(ignore[x][0]) and int(j) == int(ignore[x][1]):
                    do = 0
            if do == 1:
                addtotal += int(board[i][j])
    total = addtotal * int(last)
    return total
                                

def letsplay(board, draw, lasttime, score):
    done = [[],[]]
    ignore = []
    result = 0
    timecount = 0
    time = 0
    for x in range(0, len(board)):
        done[0].append(0)
        done[1].append(0)
    for i in range(0, len(draw)):
        timecount += 1
        present, coords = finder(board, draw[i])
        if present == 1:
            done[0][coords[0]] += 1
            done[1][coords[1]] += 1
            ignore.append(coords)
            check = donecheck(done)
            if check == 1:
                time = timecount
                last = draw[i]
                result = endcalc(board, ignore, last)
                break
    if time > lasttime:
        return time, result
    return lasttime, score
            
    

file = open('day4.txt', 'r')
lines = file.readlines()

draw = lines[0].split(",")
draw[-1] = draw[-1].strip('\n')
for y in range(0, len(draw)):
    draw[y] = int(draw[y])
del lines[0]
boardnums = int(len(lines)/6)
lasttime = 0
score = 0
for i in range(0, boardnums):
    board = []
    board.append((lines[(i*6)+1].strip()).split())
    board.append((lines[(i*6)+2].strip()).split())
    board.append((lines[(i*6)+3].strip()).split())
    board.append((lines[(i*6)+4].strip()).split())
    board.append((lines[(i*6)+5].strip()).split())
    for a in range(0, len(board)):
        for b in range(0, len(board)):
            board[a][b] = int(board[a][b])
    lasttime, score = letsplay(board, draw, lasttime, score)
print(score)
