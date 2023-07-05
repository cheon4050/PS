import sys
input = sys.stdin.readline
N, M, K = map(int, input().split())

A = [list(map(int, input().split())) for i in range(N)]
arr = [[5] * (N+1) for i in range(N+1)]
treeArr = [[[] for i in range(N+1)] for j in range(N+1)]
for i in range(M):
    x, y, z = map(int, input().split())
    treeArr[x][y].append(z)

for _ in range(K):
    for i in range(1, N+1):
        for j in range(1, N+1):
            if treeArr[i][j]:
                dieTree = []
                treeArr[i][j].sort()
                for t in range(len(treeArr[i][j])):
                    if treeArr[i][j][t] > arr[i][j]:
                        dieTree += treeArr[i][j][t:]
                        treeArr[i][j] = treeArr[i][j][:t]
                        break
                    arr[i][j] -= treeArr[i][j][t]
                    treeArr[i][j][t] += 1
                for z in dieTree:
                    arr[i][j] += z//2

    for i in range(1, N+1):
        for j in range(1, N+1):
            for t in range(len(treeArr[i][j])):
                if treeArr[i][j][t] % 5 == 0:
                    for a in range(3):
                        for b in range(3):
                            if (a == 1 and b == 1):
                                continue
                            if 1 <= i + a - 1 <= N and 1 <= j + b - 1 <= N:
                                treeArr[i+a-1][j+b-1].append(1)

    for i in range(N):
        for j in range(N):
            arr[i+1][j+1] += A[i][j]
result = 0
for i in range(1, N+1):
    for j in range(1, N+1):
        result += len(treeArr[i][j])
print(result)