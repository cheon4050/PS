N = int(input())

dp = [[0]* 10 for i in range(N+1)]

def rec(cnt, v, numDict):
    if cnt == N:
        return 1
    if dp[cnt][v]:
        return dp[cnt][v]
    total = 0
    if v != 0:
        total += rec(cnt+1, v-1, numDict)
    if v != 9:
        total += rec(cnt+1, v+1, numDict)
    dp[cnt][v] = total
    return dp[cnt][v]



result = 0
for i in range(1, 10):
    result += rec(1, i, {})
print(result%1000000000)


