from collections import deque
N, M = map(int,input().split())

arr = [list(map(int, input().split()))for i in range(N)]

def virusCheck(arr, visited, x,y, check):
    visited[x][y] = True
    q = deque([(x,y)])
    moves = [(-1, 0), (1, 0), (0, -1), (0,1)]
    cnt = 1
    while q:
        x, y = q.popleft()
        for move in moves:
            dx = x + move[0]
            dy = y + move[1]
            if 0<=dx < N and 0 <= dy < M and arr[dx][dy] == 0 and not visited[dx][dy]:
                q.append((dx,dy))
                visited[dx][dy]=True
                arr[dx][dy] = check
                cnt+=1
    return cnt

maxResult = 0
for i in range(N*M):
    for j in range(i+1, N*M):
        for k in range(j+1, N*M):
            result = 0
            arr2 = [arr[m][:] for m in range(N)]
            ax, ay = i // M, i % M
            bx, by = j // M, j % M
            cx, cy = k // M, k % M
            if arr2[ax][ay] != 0 or arr2[bx][by] != 0 or arr2[cx][cy] != 0:
                continue
            arr2[ax][ay] = 1
            arr2[bx][by] = 1
            arr2[cx][cy] = 1
            visited = [[False] * M for _ in range(N)]
            for dx in range(N):
                for dy in range(M):
                    if arr2[dx][dy] == 2 and not visited[dx][dy]:
                        virusCheck(arr2, visited, dx,dy, 2)
            for dx in range(N):
                for dy in range(M):
                    if arr2[dx][dy] == 0 and not visited[dx][dy]:
                        result += virusCheck(arr2, visited, dx, dy, 0)
            maxResult = max(result, maxResult)
print(maxResult)


