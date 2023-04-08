import sys
from collections import deque
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

K = int(input())
W, H = map(int, input().split())
INF = int(1e9)

arr = [list(map(int, input().split()))for i in range(H)]
visited = [[[INF] * W for i in range(H)] for j in range(K+1)]
horseMoves = [(1, 2), (2, 1), (-1, 2), (2, -1), (-2, 1), (1, -2),(-2, -1), (-1, -2)]
moves = [(1, 0), (0, 1),(-1, 0), (0, -1)]
def bfs():
    visited[0][0][0] = 0
    q = deque([[0, 0, 0, 0]])
    while q:
        distance, cnt, x, y = q.popleft()
        if (x, y) == (W-1, H-1):
            continue
        for move in horseMoves:
            dx = x + move[0]
            dy = y + move[1]
            if 0 <= dx < H and 0 <= dy < W and cnt < K and arr[dx][dy] == 0 and visited[cnt+1][dx][dy] > distance+1:
                visited[cnt+1][dx][dy] = distance+1
                q.append([distance+1, cnt+1, dx, dy])
        for move in moves:
            dx = x + move[0]
            dy = y + move[1]
            if 0 <= dx < H and 0 <= dy < W and arr[dx][dy] == 0 and visited[cnt][dx][dy] > distance+1:
                visited[cnt][dx][dy] = distance+1
                q.append([distance+1, cnt, dx, dy])

bfs()
result= INF
for i in range(K+1):
    result = min(result, visited[i][-1][-1])
if result == INF:
    print(-1)
else:
    print(result)