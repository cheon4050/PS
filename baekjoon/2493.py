import sys
input = sys.stdin.readline
N = int(input())

arr = list(map(int, input().split()))
stack = []
result = []
for i in range(N):
    while stack:
        if stack[-1][1] >= arr[i]:
            break
        stack.pop()
    if stack:
        result.append(stack[-1][0])
    else:
        result.append(0)
    stack.append((i+1, arr[i]))


print(*result)

