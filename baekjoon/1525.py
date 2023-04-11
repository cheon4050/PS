from collections import defaultdict, deque

import sys
sys.setrecursionlimit(10**6)
arr = [list(map(int, input().split())) for i in range(3)]

resultArr = [[i+(j*3)+1 for i in range(3)] for j in range(3)]
resultArr[-1][-1] = 0
resultArrStream = 0

for i in range(9):
    resultArrStream += resultArr[i // 3][i % 3] * (10 ** i)

dp = defaultdict(bool)

moves = [(1, 0), (0, 1), (0, -1), (-1, 0)]
result = 10000000
def bfs(x, y, arr):
    arrStream = 0
    for i in range(9):
        arrStream += arr[i // 3][i % 3] * (10 ** i)
    dp[arrStream] = True

    q = deque([(x, y, 0, arrStream)])
    while q:
        x, y, cnt, arrStream= q.popleft()
        arr = [[0] * 3 for _ in range(3)]
        for i in range(9):
            arr[i//3][i%3] = int(str(arrStream // 10**i)[-1])
        if arrStream == resultArrStream:
            return cnt
        for move in moves:
            dx = x + move[0]
            dy = y + move[1]
            if 0 <= dx < 3 and 0 <= dy < 3:
                arr[dx][dy], arr[x][y] = arr[x][y], arr[dx][dy]
                stream = 0
                for i in range(9):
                    stream += arr[i // 3][i % 3] * (10 ** i)
                arr[dx][dy], arr[x][y] = arr[x][y], arr[dx][dy]
                if dp[stream]:
                    continue
                dp[stream] = True
                q.append((dx,dy,cnt+1,stream))

    return -1

for i in range(9):
    if arr[i//3][i%3] == 0:
        print(bfs(i//3, i%3, arr))
        break