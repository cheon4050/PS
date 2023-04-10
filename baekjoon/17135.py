from collections import deque
N, M, D = map(int, input().split())

castle = [list(map(int, input().split()))for i in range(N)]
castle.append([0]*M)

moves = [(0, -1), (-1, 0), (0, 1)]
def bfs(y, arr):
    x = N
    visited = [[False] * M for _ in range(N+1)]
    visited[x][y] = True
    q = deque([(x, y, 0)])
    while q:
        x, y, cost = q.popleft()
        for move in moves:
            dx = x + move[0]
            dy = y + move[1]
            if 0 <= dx < N and 0 <= dy < M and not visited[dx][dy] and cost + 1 <= D:
                if arr[dx][dy] == 1:
                    return dx, dy
                visited[dx][dy] = True
                q.append((dx, dy, cost+1))
    return -1, -1

def play(y1, y2, y3):
    cnt = 0
    arr = [castle[i][:]for i in range(N+1)]
    for k in range(N):
        dx1, dy1 = bfs(y1, arr)
        dx2, dy2 = bfs(y2, arr)
        dx3, dy3 = bfs(y3, arr)
        if dx1 != -1 and arr[dx1][dy1] == 1:
            cnt += 1
            arr[dx1][dy1] = 0
        if dx2 != -1 and arr[dx2][dy2] == 1:
            cnt += 1
            arr[dx2][dy2] = 0
        if dx3 != -1 and arr[dx3][dy3] == 1:
            cnt += 1
            arr[dx3][dy3] = 0
        for i in range(N-1, -1, -1):
            for j in range(M-1, -1, -1):
                arr[i+1][j] = arr[i][j]
        for i in range(M):
            arr[k][i] = 0
    return cnt

result = 0
for y1 in range(M):
    for y2 in range(M):
        for y3 in range(M):
            if y1 == y2 or y2 == y3 or y1 == y3:
                continue
            result = max(result, play(y1,y2,y3))
print(result)