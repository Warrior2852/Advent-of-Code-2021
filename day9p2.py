def floodfill(coords, visited, rows, num, maxwidth, maxheight):
    if coords in visited or rows[coords[0]][coords[1]] == 9:
        return num
    num += 1
    visited.append(coords)
    if coords[0] != maxheight:
        newcoords = ([coords[0]+1, coords[1]])
        num = floodfill(newcoords, visited, rows, num, maxwidth, maxheight)
    if coords[0] != 0:
        newcoords = ([coords[0]-1, coords[1]])
        num = floodfill(newcoords, visited, rows, num, maxwidth, maxheight)
    if coords[1] != 0:
        newcoords = ([coords[0], coords[1]-1])
        num = floodfill(newcoords, visited, rows, num, maxwidth, maxheight)
    if coords[1] != maxwidth:
        newcoords = ([coords[0], coords[1]+1])
        num = floodfill(newcoords, visited, rows, num, maxwidth, maxheight)
    return num

file = open('day9.txt', 'r')
lines = file.readlines()
rows = []

for row in lines:
    temprow = []
    for a in range(0, len(row)):
        temprow.append(row[a])
    del temprow[-1]
    for b in range(0, len(temprow)):
        temprow[b] = int(temprow[b])
    rows.append(temprow)

lowpoints = []
maxwidth = len(rows[0])-1
maxheight = len(rows)-1
for x in range(0, len(rows)):
    for y in range(0, len(rows[0])):
        if x == 0 and y == 0:
            if rows[x][y] < rows[x][y+1] and rows[x][y] < rows[x+1][y]:
                lowpoints.append([x, y])
        elif x == 0 and y == maxwidth:
            if rows[x][y] < rows[x][y-1] and rows[x][y] < rows[x+1][y]:
                lowpoints.append([x, y])
        elif x == 0:
            if rows[x][y] < rows[x][y+1] and rows[x][y] < rows[x][y-1] and rows[x][y] < rows[x+1][y]:
                lowpoints.append([x, y])
        elif x == maxheight and y == 0:
            if rows[x][y] < rows[x][y+1] and rows[x][y] < rows[x-1][y]:
                lowpoints.append([x, y])
        elif x == maxheight and y == maxwidth:
            if rows[x][y] < rows[x][y-1] and rows[x][y] < rows[x-1][y]:
                lowpoints.append([x, y])
        elif y == maxwidth:
            if rows[x][y] < rows[x+1][y] and rows[x][y] < rows[x][y-1] and rows[x][y] < rows[x-1][y]:
                lowpoints.append([x, y])
        elif y == 0:
            if rows[x][y] < rows[x][y+1] and rows[x][y] < rows[x+1][y] and rows[x][y] < rows[x-1][y]:
                lowpoints.append([x, y])
        elif x == maxheight:
            if rows[x][y] < rows[x][y+1] and rows[x][y] < rows[x][y-1] and rows[x][y] < rows[x-1][y]:
                lowpoints.append([x, y])
        else:
            if rows[x][y] < rows[x][y+1] and rows[x][y] < rows[x][y-1] and rows[x][y] < rows[x-1][y] and rows[x][y] < rows[x+1][y]:
                lowpoints.append([x, y])

third = 0
second = 0
first = 0
for i in range(0, len(lowpoints)):
    visited = []
    lowpoint = lowpoints[i]
    num = 0
    num = floodfill(lowpoint, visited, rows, num, maxwidth, maxheight)
    if num > third:
        third = num
        if num > second:
            temp = second
            second = num
            third = temp
            if num > first:
                temp = first
                first = num
                second = temp
    
result = first * second * third
print(result)
