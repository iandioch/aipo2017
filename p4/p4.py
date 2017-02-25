h, w = (int(c) for c in input().split())
g = [input() for i in range(h)]

dp = [[0 for x in range(w)] for y in range(h)]
for x in range(w):
    if g[0][x] == 'X':
        break
    dp[0][x] = 1
for y in range(1, h):
    if g[y][0] == 'X':
        break
    dp[y][0] = 1

for y in range(1, h):
    for x in range(1, w):
        if g[y][x] == 'X':
            continue
        dp[y][x] = dp[y-1][x] + dp[y][x-1]
print(dp[-1][-1])
