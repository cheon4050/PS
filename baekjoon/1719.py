import sys
input = sys.stdin.readline

n, k = map(int, input().split())
INF = int(1e9)
graph = [[INF] * (n+1)for i in range(n+1)]

arr = [[INF] * (n+1) for i in range(n+1)]

for i in range(k):
    a, b, c = map(int, input().split())
    graph[a][b] = c
    graph[b][a] = c
    arr[a][b] = b
    arr[b][a] = a

for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            if graph[i][j] > graph[i][k] + graph[k][j]:
                graph[i][j] = graph[i][k] + graph[k][j]
                arr[i][j] = arr[i][k]
                arr[j][i] = arr[j][k]

for i in range(1, n+1):
    arr[i][i] = "-"

for i in range(1, n+1):
    for k in range(1, n+1):
        print(arr[i][k], end = " ")
    print()