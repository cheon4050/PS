from heapq import heappop, heappush
import sys
input = sys.stdin.readline
v, e = map(int, input().split())

# graph = [[100000000] * (v+1) for i in range(v+1)]
#
# for i in range(1, v+1):
#     for j in range(1, v+1):
#         if i == j:
#             graph[i][j] = 0
#
# for i in range(e):
#     a, b, cost = map(int, input().split())
#     graph[a][b]=cost
#
#
# for k in range(1, v+1):
#     for i in range(1, v+1):
#         for j in range(1, v+1):
#             graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])
#
# result = 100000000
# for i in range(1, v+1):
#     for j in range(i+1, v+1):
#         result = min(result, graph[i][j] + graph[j][i])
# if result == 100000000:
#     result = -1
# print(result)


graph = [[] for i in range(v+1)]
distance = [[100000000] * (v+1) for i in range(v+1)]

for i in range(e):
    a, b, cost = map(int, input().split())
    graph[a].append((b, cost))

h = []


def dijkstra(start, distance):
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

for i in range(1, v+1):
    dijkstra(i, distance[i])

result = 100000000
for i in range(1, v+1):
    for j in range(i+1, v+1):
        result = min(result, distance[i][j] + distance[j][i])
if result == 100000000:
    result = -1
print(result)

