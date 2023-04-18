from collections import deque
from heapq import heappush, heappop
import sys
input = sys.stdin.readline
N = int(input())
INF = int(1e9)
graph = [[] for i in range(N+1)]
depth = [0] * (N+1)
parents = [0] * (N+1)
distance = [INF] * (N+1)
for _ in range(N-1):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))
def dijkstra(start):
    q = []

    heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heappush(q, (cost, i[0]))

def bfs(s):
    visited = [False] * (N+1)
    queue = deque()
    queue.append(s)
    while queue:
        node = queue.popleft()
        visited[node] = True
        for i in graph[node]:
            if not visited[i[0]]:
                depth[i[0]] = depth[node] + 1
                parents[i[0]] = node
                queue.append(i[0])

def LCA(a,b):
    if depth[a] < depth[b]:
        temp = a
        a=b
        b=temp
    diff = depth[a] - depth[b]
    for _ in range(diff):
        a = parents[a]
    while a!=b:
        a = parents[a]
        b = parents[b]
    return a


M = int(input())
dijkstra(1)
bfs(1)
for i in range(M):
    a, b = map(int,input().split())
    parent = LCA(a, b)
    print(distance[a] + distance[b] - 2 * distance[parent])



