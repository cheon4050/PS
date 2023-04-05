import sys
input = sys.stdin.readline
N = int(input())

arr = []
for _ in range(N):
    i, a = map(int, input().split())
    arr.append((i,a))
arr.sort(key = lambda x : x[0])
prefixSum = [arr[0][1]]
prefixSumReverse = [arr[-1][1]]

for i in range(1, N):
    prefixSum.append(prefixSum[i-1] + arr[i][1])
    prefixSumReverse.append(prefixSumReverse[i-1] + arr[-i-1][1])

prefixSumReverse = prefixSumReverse[::-1]
result = [0] * N
for i in range(1,N):
    result[0] += abs(arr[i][0] - arr[i-1][0]) * prefixSumReverse[i]

minResult = [arr[0][0], result[0]]

for i in range(1, N):
    result[i] = result[i-1] + abs(arr[i][0] - arr[i-1][0]) * prefixSum[i-1] - abs(arr[i][0] - arr[i-1][0]) * prefixSumReverse[i]

    if minResult[1] > result[i]:
        minResult[0] = arr[i][0]
        minResult[1] = result[i]

print(minResult[0])