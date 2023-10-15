from collections import deque

x, y = map(int, input().split())

arr = [list(map(int, input().split()))for i in range(x)]

def check(x, y, arr):
    moves = [(-1, 0), (1, 0), (0, 1), (0, -1)]
    for move in moves:
        dx = x + move[0]
        dy = y + move[1]
        if arr[dx][dy] == 2:
            return True
    return False

def bfs2(x, y, arr, visited):
    visited[x][y] = True
    moves = [(-1, 0), (1, 0), (0, 1), (0, -1)]
    q = deque([(x, y)])
    cnt = 0
    while q:
        x, y = q.popleft()
        for move in moves:
            dx = x + move[0]
            dy = y + move[1]
            if 0 <= dx < len(arr) and 0 <= dy < len(arr[0]) and (arr[dx][dy] == 0 or arr[dx][dy] == 2) and not visited[dx][dy]:
                visited[dx][dy] = True
                arr[dx][dy] = 2
                q.append((dx, dy))

def bfs(x, y, arr, visited):
    visited[x][y] = True
    removeCheese = []
    moves = [(-1, 0), (1, 0), (0, 1), (0, -1)]
    q = deque([(x, y)])
    cnt = 0
    while q:
        x, y = q.popleft()
        if check(x, y, arr):
            cnt += 1
            removeCheese.append((x, y))
        for move in moves:
            dx = x + move[0]
            dy = y + move[1]
            if 0 <= dx < len(arr) and 0 <= dy < len(arr[0]) and arr[dx][dy] == 1 and not visited[dx][dy]:
                visited[dx][dy] = True
                q.append((dx, dy))
    return removeCheese
count = 0
for i in range(len(arr)):
    for j in range(len(arr[0])):
        if arr[i][j] == 1:
            count += 1

result = []
time = 0
visited = [[False] * len(arr[0]) for i in range(len(arr))]
while True:
    visited = [[False] * len(arr[0]) for i in range(len(arr))]
    bfs2(0, 0, arr, visited)
    visited = [[False] * len(arr[0]) for i in range(len(arr))]
    removeCheese = []
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            if arr[i][j] == 1:
                removeCheese += bfs(i, j,arr, visited)

    removeCheese = list(set(removeCheese))
    for a, b in removeCheese:
        arr[a][b] = 0

    cnt = len(removeCheese)
    result.append(cnt)
    if cnt == 0:
        break
    time += 1
print(time)
print(result[-2])
