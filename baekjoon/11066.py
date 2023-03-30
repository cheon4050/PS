T = int(input())

for _ in range(T):
    N = int(input())
    arr = list(map(int, input().split()))
    prefixSum = [0]
    for i in range(N):
        prefixSum.append(prefixSum[-1] + arr[i])
    dp = [[0] * (N+1) for i in range(N+1)]
    for i in range(2,N+1):
        for j in range(1, N+2-i):
            dp[j][j+i-1] = min(dp[j][j+k] + dp[j+k+1][j+i-1] for k in range(i-1)) + (prefixSum[j+i-1]- prefixSum[j-1])
    print(dp[1][N])
