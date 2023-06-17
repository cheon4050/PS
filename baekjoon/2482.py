N = int(input())
K = int(input())

mod = 1000000003
dp = [[0] * (K+1) for i in range(N+1)]

for i in range(N+1):
    dp[i][0] = 1
    dp[i][1] = i

for i in range(2, N+1):
    for j in range(2, K+1):
        if i == N:
            dp[i][j] = dp[i-1][j] + dp[i-3][j-1]
        else:
            dp[i][j] = dp[i-1][j] + dp[i-2][j-1]
        dp[i][j] %= mod

print(dp[N][K])
