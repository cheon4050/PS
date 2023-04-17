from collections import deque

N = int(input())

time = [0] * (N+1)
indegree = [0] * (N+1)
graph = [[] for i in range(N+1)]
for i in range(1,N+1):
    arr = list(map(int, input().split()))
    time[i] = arr[0]
    arr = arr[1:-1]
    for k in arr:
        indegree[i] += 1
        graph[k].append(i)

result = [0] * (N+1)
def topology_sort():
    q = deque()

    for i in range(1, N+1):
        if indegree[i] == 0:
            result[i] = time[i]
            q.append(i)

    while q:
        now = q.popleft()
        for i in graph[now]:
            indegree[i] -= 1
            result[i] = max(result[i], result[now] + time[i])
            if indegree[i] == 0:
                q.append(i)

topology_sort()
for i in range(1, N+1):
    print(result[i])
