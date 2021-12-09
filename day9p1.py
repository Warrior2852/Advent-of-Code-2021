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

lowpoints = 0
maxwidth = len(rows[0])-1
maxheight = len(rows)-1
for x in range(0, len(rows)):
    for y in range(0, len(rows[0])):
        if x == 0 and y == 0:
            if rows[x][y] < rows[x][y+1] and rows[x][y] < rows[x+1][y]:
                lowpoints = lowpoints + rows[x][y] + 1
        elif x == 0 and y == maxwidth:
            if rows[x][y] < rows[x][y-1] and rows[x][y] < rows[x+1][y]:
                lowpoints = lowpoints + rows[x][y] + 1
        elif x == 0:
            if rows[x][y] < rows[x][y+1] and rows[x][y] < rows[x][y-1] and rows[x][y] < rows[x+1][y]:
                lowpoints = lowpoints + rows[x][y] + 1
        elif x == maxheight and y == 0:
            if rows[x][y] < rows[x][y+1] and rows[x][y] < rows[x-1][y]:
                lowpoints = lowpoints + rows[x][y] + 1
        elif x == maxheight and y == maxwidth:
            if rows[x][y] < rows[x][y-1] and rows[x][y] < rows[x-1][y]:
                lowpoints = lowpoints + rows[x][y] + 1
        elif y == maxwidth:
            if rows[x][y] < rows[x+1][y] and rows[x][y] < rows[x][y-1] and rows[x][y] < rows[x-1][y]:
                lowpoints = lowpoints + rows[x][y] + 1
        elif y == 0:
            if rows[x][y] < rows[x][y+1] and rows[x][y] < rows[x+1][y] and rows[x][y] < rows[x-1][y]:
                lowpoints = lowpoints + rows[x][y] + 1
        elif x == maxheight:
            if rows[x][y] < rows[x][y+1] and rows[x][y] < rows[x][y-1] and rows[x][y] < rows[x-1][y]:
                lowpoints = lowpoints + rows[x][y] + 1
        else:
            if rows[x][y] < rows[x][y+1] and rows[x][y] < rows[x][y-1] and rows[x][y] < rows[x-1][y] and rows[x][y] < rows[x+1][y]:
                lowpoints = lowpoints + rows[x][y] + 1
print(lowpoints)

