N, M, H = map(int, input().split())

arr = [[i for i in range(N+1)]for i in range(H+1)]

def check(arr):
    for i in range(1, N + 1):
        y = i
        x = 1
        while x <= H:
            y = arr[x][y]
            x += 1
        if y != i:
            return False
    return True

for i in range(M):
    a, b = map(int, input().split())
    arr[a][b] = b+1
    arr[a][b+1] = b
result = 100
def req(arr, cnt, k):
    global result
    if cnt > 3:
        return 100
    if result <= cnt:
        return result
    if check(arr):
        result = cnt
        return cnt
    for x in range(k+1, (N+1)*(H+1)):
        i = x // (N+1)
        j = x % (N+1)
        if j == N:
            continue
        if arr[i][j] == j and arr[i][j+1] == j+1:
            arr[i][j] = j+1
            arr[i][j+1] = j
            result = min(result, req(arr,cnt + 1, x))
            arr[i][j] = j
            arr[i][j + 1] = j + 1
    return result

req(arr, 0, 0)
if result == 100:
    print(-1)
else:
    print(result)