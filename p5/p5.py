g = [[99999999 for y in range(8)] for x in range(8)]
start = input()
end = input()
start_x = ord(start[0])-ord('a')
start_y = int(start[1]) - 1
end_x= ord(end[0])-ord('a')
end_y = int(end[1]) - 1

bfs = [(0, start_x, start_y)]
bfs = {(start_x, start_y) : 0}

def try_to_add(d, x, y):
    if (x, y) in bfs:
        if d < bfs[(x, y)]:
            bfs[(x, y)] = d
    else:
        bfs[(x, y)] = d

while True:
    k = sorted(bfs.keys(), key = lambda x: bfs[x])
    x, y = k[0]
    d = bfs[k[0]]
    del bfs[k[0]]
    if x < 0 or y < 0 or x > 8 or y > 8:
        continue
    if x == end_x and y == end_y:
        print(d)
        break
    
    try_to_add(d+1, x+2, y+1)
    try_to_add(d+1, x+2, y-1)
    try_to_add(d+1, x-2, y+1)
    try_to_add(d+1, x-2, y-1)
    try_to_add(d+1, x+1, y+2)
    try_to_add(d+1, x+1, y-2)
    try_to_add(d+1, x-1, y+2)
    try_to_add(d+1, x-1, y-2)
