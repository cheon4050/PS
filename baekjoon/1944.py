from collections import deque
N, M = map(int, input().split())

arr = [list(input()) for i in range(N)]

nodeList = []
cnt = 0
nodeDict = {}
for i in range(N):
    for j in range(N):
        if arr[i][j] == "S" or arr[i][j] == "K":
            nodeDict[(i, j)] = cnt
            cnt +=1


def bfs(arr, x, y):
    visited = [[False] * N for i in range(N)]
    visited[x][y] = True
    moves = [(-1, 0), (1, 0), (0, 1), (0, -1)]
    start_index = nodeDict[(x, y)]
    q = deque([(0, x, y)])
    result = []
    while q:
        cost, x, y = q.popleft()
        for move in moves:
            dx = x + move[0]
            dy = y + move[1]
            if arr[dx][dy] != "1" and not visited[dx][dy]:
                visited[dx][dy] = True
                if arr[dx][dy] == "S" or arr[dx][dy] == "K":
                    result.append((cost+1, start_index, nodeDict[(dx,dy)]))
                    continue
                q.append((cost+1, dx, dy))

    return result

edges = []

for x, y in nodeDict.keys():
    edges += bfs(arr, x, y)

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

parent = [0] * (M+1)

for i in range(1, M+1):
    parent[i] = i

edges.sort()

result = 0
edge_cnt = 0
for edge in edges:
    cost, a, b = edge
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        edge_cnt += 1
        result += cost
if edge_cnt != M:
    result = -1
print(result)