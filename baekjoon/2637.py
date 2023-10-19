from collections import deque

v = int(input())
e = int(input())

indegree = [0] * (v+1)

graph = [[]for i in range(v+1)]
middleParts = [False] * (v+1)
for _ in range(e):
    a, b, c = map(int, input().split())
    middleParts[a] = True
    graph[a].append((b, c))

    indegree[b] += 1

def topology_sort():
    result = [0] * (v+1)
    result[v] = 1
    q = deque()
    q.append(v)
    while q:
        now= q.popleft()
        for i in graph[now]:
            next = i[0]
            cost = i[1]
            indegree[next] -= 1
            result[next] += cost * result[now]
            if indegree[next] == 0:
                q.append(next)
    return result

result = topology_sort()

for i in range(1, v):
    if not middleParts[i]:
        print(i, result[i])