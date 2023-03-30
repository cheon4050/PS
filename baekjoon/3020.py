from collections import Counter
N, H = map(int, input().split())

prefixSum = [0]*(H+1)

for i in range(N):
    a = int(input())

    if i%2:
        prefixSum[0] += 1
        prefixSum[a] -= 1
    else:
        prefixSum[H] -= 1
        prefixSum[H-a] += 1
for i in range(H):
    prefixSum[i+1] = prefixSum[i] + prefixSum[i+1]
prefixSum = prefixSum[:-1]
minResult = min(prefixSum)
minCount = 0
for i in prefixSum:
    if i == minResult:
        minCount += 1
print(minResult, minCount)