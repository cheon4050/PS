N, M = map(int, input().split())

m = list(map(int, input().split()))
c = list(map(int, input().split()))

dp = [[0]*(sum(c)+1) for i in range(N+1)]

for i in range(1, N+1):
    memory = m[i-1]
    cost = c[i-1]
    for j in range(1, sum(c)+1):
        if cost > j:
            dp[i][j] = dp[i-1][j]
            continue
        dp[i][j] = max(memory + dp[i-1][j-cost], dp[i-1][j])

for i in range(sum(c)+1):
    if dp[-1][i] >= M:
        print(i)
        break


