import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
N = int(input())

arr = [[] for i in range(N+1)]
for i in range(N-1):
    a, b, c = map(int, input().split())
    arr[a].append((b, c))

distance = [[] for i in range(N+1)]
def dfs(v):
    result = 0
    for x, cost in arr[v]:
        cnt = dfs(x) + cost
        distance[v].append(cnt)
        result = max(result, cnt)
    return result

dfs(1)
result = 0
for dist in distance:
    if len(dist) > 1:
        dist.sort()
        result = max(result, dist[-1] + dist[-2])
    elif len(dist) == 1:
        result = max(result, dist[-1])

print(result)
