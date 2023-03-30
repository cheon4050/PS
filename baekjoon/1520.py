import sys
input = sys.stdin.readline
N, M = map(int, input().split())

arr = [list(map(int, input().split())) for i in range(N)]

visited = [[-1] * M for i in range(N)]

moves = [(1, 0), (-1, 0), (0, 1), (0, -1)]

def dp(x, y):
    if x == N-1 and y == M-1:
        return 1

    if visited[x][y] != -1:
        return visited[x][y]
    sum = 0
    for move in moves:
        dx = x + move[0]
        dy = y + move[1]
        if 0 <= dx < N and 0 <= dy < M and arr[x][y] > arr[dx][dy]:
            sum += dp(dx, dy)
    visited[x][y] = sum
    return visited[x][y]

dp(0, 0)
print(visited[0][0])