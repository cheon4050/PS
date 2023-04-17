import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

N = int(input())
A, B, C = map(int, input().split())
M = int(input())

graph = [[] for i in range(N+1)]

for _ in range(M):
    a, b, c = map(int, input().split())
    graph[a].append((b,c))
    graph[b].append((a,c))

def dijkstra(start):
    distance = [INF] * (N + 1)
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)

        if distance[now] < dist:
            continue

        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))
    return distance

distanceA = dijkstra(A)
distanceB = dijkstra(B)
distanceC = dijkstra(C)

result = 0
minNum = 0
for i in range(1, N+1):
    if min(distanceA[i], distanceB[i], distanceC[i]) > minNum:
        minNum = min(distanceA[i], distanceB[i], distanceC[i])
        result = i
print(result)