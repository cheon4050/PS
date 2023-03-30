import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N = int(input())
    arr = []
    cnt = 1
    for i in range(N):
        arr.append(list(map(int, input().split())))
    arr.sort()
    minRank = arr[0][1]
    for i in range(N):
        if arr[i][1] < minRank:
            minRank = arr[i][1]
            cnt+=1

    print(cnt)


