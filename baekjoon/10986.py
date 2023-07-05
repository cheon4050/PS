from collections import defaultdict
N, M = map(int, input().split())

arr = list(map(int,input().split()))

prefixSum = [0]
result = 0
counter = defaultdict(int)
for i in range(N):
    num = (prefixSum[-1] + arr[i])%M
    counter[num] += 1
    prefixSum.append(num)

mod = 0

for i in range(N):
    result += counter[mod]
    mod = (arr[i] + mod) % M
    counter[prefixSum[i+1]] -= 1

print(result)