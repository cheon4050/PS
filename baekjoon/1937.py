import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
N = int(input())
arr = [list(map(int, input().split()))for i in range(N)]

moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]
def dfs(arr, visited, x, y):
    if visited[x][y] != 0:
        return visited[x][y]
    result = 0
    for move in moves:
        dx = x + move[0]
        dy = y + move[1]
        if 0 <= dx < N and 0 <= dy < N and arr[dx][dy] > arr[x][y]:
            result = max(result, dfs(arr, visited, dx, dy))
    visited[x][y] = result + 1
    return visited[x][y]

result = 0
visited = [[0] * N for i in range(N)]
for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            result = max(result, dfs(arr,visited, i, j))
print(result)
