N = int(input())
k = int(input())

def solve(x):
    cnt = 0
    for i in range(1, N+1):
        cnt += min(x//i, N)
    return cnt

start = 0
end = N*N
result= 0
while start <= end:
    mid = (start + end) // 2
    cnt = solve(mid)
    if cnt < k:
        start = mid+1
    else:
        result = mid
        end = mid - 1
print(result)


