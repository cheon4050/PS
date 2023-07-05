N = int(input())
arr = list(map(int, input().split()))

result = [-1] * N
stack =[]
for i in range(N):
    while stack and stack[-1][1] < arr[i]:
        index, num = stack.pop()
        result[index] = arr[i]
    stack.append((i, arr[i]))
print(*result)