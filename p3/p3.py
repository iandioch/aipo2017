h, w = (int(c) for c in input().split())
lines = [[int(c) for c in input().strip()] for i in range(h)]
after = [[c for c in line] for line in lines]

def fillat(x, y, startx, starty, col):
    if after[x][y] != lines[startx][starty]:
        return
    after[x][y] = col
    if x > 0:
        fillat(x-1, y, startx, starty, col)
    if x < len(lines) - 1:
        fillat(x+1, y, startx, starty, col)
    if y > 0:
        fillat(x, y-1, startx, starty, col)
    if y < len(lines[0]) - 1:
        fillat(x, y+1, startx, starty, col)

x, y, col = (int(c) for c in input().split())

fillat(x, y, x, y, col)
for line in after:
    print (''.join([str(c) for c in line]))
