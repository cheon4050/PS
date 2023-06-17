import sys
input = sys.stdin.readline
N = int(input())

arr = list(map(int,input().split()))

size = int(input())

sumArr = []
for i in range(N-size+1):
    sumArr.append(sum(arr[i:i+size]))

dp = [[0] * (len(sumArr)) for i in range(4)]

dp[1][0] = sumArr[0]
for i in range(1,4):
    for j in range(size, len(sumArr)):
        dp[i][j] = max(dp[i-1][j-size]+sumArr[j], dp[i][j-1])

print(dp[-1][-1])
