from heapq import heappush, heappop
M, N = map(int, input().split())

arr = []
for _ in range(N):
    arr.append(list(map(int, list(input()))))

visited = [[0] * M for i in range(N)]

def bfs(vx, vy, visited, arr):
    q = []
    heappush(q, (1,[vx, vy]))
    visited[vx][vy]= 1
    moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    while q:
        cnt, xy = heappop(q)
        x, y = xy[0], xy[1]
        for move in moves:
            dx = x + move[0]
            dy = y + move[1]
            if 0 <= dx < N and 0 <= dy < M and visited[dx][dy] == 0:
                if arr[dx][dy] == 1:
                    visited[dx][dy] = cnt + 1
                else:
                    visited[dx][dy] = cnt
                heappush(q, (visited[dx][dy], [dx,dy]))
            if dx == N-1 and dy == M-1:
                return

bfs(0, 0, visited, arr)
print(visited[N - 1][M - 1] - 1)