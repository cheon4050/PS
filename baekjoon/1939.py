from collections import defaultdict
from heapq import heappush, heappop
import sys
input = sys.stdin.readline
N, M = map(int, input().split())

INF = int(1e9)+1
graph = [defaultdict(int) for i in range(N+1)]

for _ in range(M):
    a, b, c = map(int,input().split())
    graph[a][b] = max(graph[a][b], c)
    graph[b][a] = graph[a][b]

start, end = map(int, input().split())

distance = [-1] * (N+1)
def dfs(v):
    q = []
    heappush(q, (-INF, start))
    distance[v] = INF
    while q:
        dist, now = heappop(q)
        dist = -dist
        if distance[now] > dist:
            continue
        for i in graph[now]:

            cost = dist
            if cost > graph[now][i]:
                cost = graph[now][i]
            if cost > distance[i]:
                distance[i] = cost
                heappush(q, (-cost, i))
    return distance[end]

print(dfs(start))