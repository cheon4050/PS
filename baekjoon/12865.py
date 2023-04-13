N, K = map(int, input().split())
arr = []
for i in range(N):
    w, v = map(int, input().split())
    arr.append((w, v))

dp = [[0] * (K+1) for i in range(N+1)]

for i in range(1, N+1):
    w, v = arr[i-1][0], arr[i-1][1]
    for k in range(1, K+1):
        if w > k:
            dp[i][k] = dp[i-1][k]
            continue
        dp[i][k] = max(dp[i-1][k], dp[i-1][k-w] + v)
print(dp[-1][-1])
