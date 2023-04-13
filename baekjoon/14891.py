from collections import deque

arr = [deque(list(map(int, list(input())))) for i in range(4)]

arr.insert(0, [])

K = int(input())
for _ in range(K):
    a, direction = map(int, input().split())
    x, y = arr[a][2], arr[a][6]
    check = [0, 0, 0, 0, 0]
    check[a] = direction
    d = direction
    for i in range(a, 1, -1):
        if arr[i][6] == arr[i-1][2]:
            break

        check[i-1] = -d
        d = -d
    d = direction
    for i in range(a, 4):
        if arr[i][2] == arr[i+1][6]:
            break
        check[i+1] = -d
        d = -d
    for i in range(1, 5):
        if check[i] == 1:
            arr[i].appendleft(arr[i].pop())
        if check[i] == -1:
            arr[i].append(arr[i].popleft())

result = 0
for i in range(1, 5):
    if arr[i][0] == 1:
        result += 2 ** (i-1)
print(result)



