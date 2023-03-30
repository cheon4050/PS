from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
indegree = [0]*(N+1)
graph = [[] for i in range(N+1)]
dp = [0] * (N+1)
for i in range(1, N+1):
    task = list(map(int, input().split()))
    cost = task[0]
    dp[i]=cost
    for j in range(task[1]):
        graph[task[j+2]].append((i,cost))
        indegree[i] += 1

def topology_sort():
    q = deque()
    for i in range(1, N+1):
        if indegree[i] == 0:
            q.append(i)

    while q:
        now = q.popleft()
        for i, cost in graph[now]:
            indegree[i] -=1
            dp[i] = max(dp[i], dp[now] + cost)
            if indegree[i] ==0:
                q.append(i)
    print(max(dp))
topology_sort()