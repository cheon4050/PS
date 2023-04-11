import sys
from collections import Counter
input = sys.stdin.readline
N = int(input())
arr = list(map(int, input().split()))
counter = Counter(arr)
stack = [(arr[0], 0)]
result =[-1] * N
for i in range(1, N):
    while stack and counter[stack[-1][0]] < counter[arr[i]]:
        num, index = stack.pop()
        result[index] = arr[i]
    stack.append((arr[i], i))
print(*result)