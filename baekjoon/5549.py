import sys
input = sys.stdin.readline
M, N = map(int, input().split())

K = int(input())

arr = [list(input().rstrip()) for i in range(M)]
JPrefixSum = [[0] * (N+1) for i in range(M+1)]
OPrefixSum = [[0] * (N+1) for i in range(M+1)]
IPrefixSum = [[0] * (N+1) for i in range(M+1)]

for i in range(M):
    for j in range(N):
        if arr[i][j] == "J":
            JPrefixSum[i+1][j+1] = 1
        elif arr[i][j] == "O":
            OPrefixSum[i+1][j+1] = 1
        elif arr[i][j] == "I":
            IPrefixSum[i+1][j+1] = 1

for i in range(1, M+1):
    for j in range(2, N+1):
        JPrefixSum[i][j] = JPrefixSum[i][j] + JPrefixSum[i][j-1]
        OPrefixSum[i][j] = OPrefixSum[i][j] + OPrefixSum[i][j-1]
        IPrefixSum[i][j] = IPrefixSum[i][j] + IPrefixSum[i][j-1]

for i in range(2, M+1):
    for j in range(1, N+1):
        JPrefixSum[i][j] = JPrefixSum[i][j] + JPrefixSum[i-1][j]
        OPrefixSum[i][j] = OPrefixSum[i][j] + OPrefixSum[i-1][j]
        IPrefixSum[i][j] = IPrefixSum[i][j] + IPrefixSum[i-1][j]

for _ in range(K):
    a, b, c, d = map(int, input().split())
    jCnt = JPrefixSum[c][d] - JPrefixSum[a-1][d] - JPrefixSum[c][b-1] + JPrefixSum[a-1][b-1]
    oCnt = OPrefixSum[c][d] - OPrefixSum[a-1][d] - OPrefixSum[c][b-1] + OPrefixSum[a-1][b-1]
    iCnt = IPrefixSum[c][d] - IPrefixSum[a-1][d] - IPrefixSum[c][b-1] + IPrefixSum[a-1][b-1]
    print(jCnt, oCnt, iCnt)

