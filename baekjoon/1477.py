N, M, L = map(int, input().split())

arr = [0] + list(map(int, input().split())) + [L]

arr.sort()

arr2=[]
for i in range(len(arr)-1):
    arr2.append(arr[i+1]-arr[i])
arr2.sort()

dp = [1] * len(arr2)
while M > 0:
    M -= 1
    maxResult = (0, -1)
    for i in range(len(arr2)):
        a = arr2[i] // dp[i]
        if arr2[i] % dp[i]:
            a += 1
        if maxResult[0] < a:
            maxResult = (a, i)
    dp[maxResult[1]] += 1

result = 0
for i in range(len(arr2)):
    a = arr2[i] // dp[i]
    if arr2[i] % dp[i]:
        a += 1
    result = max(result, a)
print(result)


