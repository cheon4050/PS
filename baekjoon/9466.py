import sys
sys.setrecursionlimit(10**9)
T = int(input())
def dfs(v, arr, visited, visitedArr):
    visitedArr.append(v)
    visited[v] = True
    if visited[arr[v]-1]:
        if not arr[v]-1 in visitedArr:
            return 0
        startIndex = visitedArr.index(arr[v]-1)
        return len(visitedArr) - startIndex
    return dfs(arr[v]-1, arr, visited, visitedArr)

for _ in range(T):
    N = int(input())
    arr = list(map(int, input().split()))
    visited = [False] * (N)
    sum = 0
    for i in range(N):
        if not visited[i]:
            sum += dfs(i, arr, visited, [])
    print(N-sum)