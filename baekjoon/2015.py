from collections import defaultdict

N, K = map(int, input().split())

arr = list(map(int, input().split()))

prefixSum = [0] * (N+1)

for i in range(N):
    prefixSum[i+1] = prefixSum[i] + arr[i]

numDict = defaultdict(int)

result = 0
for i in range(N, 0, -1):
    SUM = prefixSum[i]
    if SUM == K:
        result +=1

    target = SUM+K
    result += numDict[target]

    numDict[SUM]+=1

print(result)
