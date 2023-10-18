import sys
input = sys.stdin.readline
N, M, K = map(int, input().split())
arr = [list(input())for i in range(N)]

check = [[0] * M for i in range(N)]
check2 = [[0] * M for i in range(N)]
for i in range(N):
    for j in range(M):
        if (i + j) %2 == 0:
            check[i][j] = "B"
            check2[i][j] = "W"
        else:
            check[i][j] = "W"
            check2[i][j] = "B"

prefixSum = [[0] * (M+1) for i in range(N+1)]
prefixSum2 = [[0] * (M+1) for i in range(N+1)]


for i in range(1, N+1):
    for j in range(1, M+1):
        if arr[i-1][j-1] != check[i-1][j-1]:
            prefixSum[i][j] = 1
        if arr[i-1][j-1] != check2[i-1][j-1]:
            prefixSum2[i][j] = 1

for i in range(1, N+1):
    for j in range(2, M+1):
        prefixSum[i][j] = prefixSum[i][j-1] + prefixSum[i][j]
        prefixSum2[i][j] = prefixSum2[i][j-1] + prefixSum2[i][j]
for i in range(2,N+1):
    for j in range(1, M+1):
        prefixSum[i][j] = prefixSum[i-1][j] + prefixSum[i][j]
        prefixSum2[i][j] = prefixSum2[i-1][j] + prefixSum2[i][j]

result = 100000000
for i in range(1, N-K+2):
    for j in range(1, M-K+2):
        result = min(result, prefixSum[i+K-1][j+K-1] - prefixSum[i+K-1][j-1] - prefixSum[i-1][j+K-1] + prefixSum[i-1][j-1])
        result = min(result, prefixSum2[i+K-1][j+K-1] - prefixSum2[i+K-1][j-1] - prefixSum2[i-1][j+K-1] + prefixSum2[i-1][j-1])
print(result)

