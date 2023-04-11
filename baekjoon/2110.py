import sys
input = sys.stdin.readline
N, C = map(int, input().split())
arr = []
for i in range(N):
    arr.append(int(input()))

arr.sort()


start = 1
end = int(1e9)
result= 0
while start <= end:
    cnt = 1
    mid = (start + end) // 2
    index = 0
    for i in range(1, N):
        if arr[i]-arr[index] >= mid:
            index = i
            cnt+=1
    if cnt < C:
        end = mid - 1
    else:
        result = max(result, mid)
        start = mid + 1

print(result)


