import heapq
import sys
from collections import deque
input = sys.stdin.readline
N = int(input())

arr = [list(map(int, input().split())) for i in range(N)]
arr.sort()

result = 0
resultTime = [0, 2100000000]

# startTimes = deque()
endTimes = []
cnt = 0
previousCnt= 0
for i in range(N):
    te, tx = arr[i]
    previousCnt = cnt
    cnt += 1
    flag=False
    # startTimes.append(te)
    heapq.heappush(endTimes, tx)
    while endTimes:
        if endTimes[0] > te:
            break
        if endTimes[0] == te:
            flag = True
        heapq.heappop(endTimes)
        # startTimes.popleft()
        cnt -= 1
    # heapq.heappush(endTimes, tx)
    if cnt > result:
        result = cnt
        resultTime = [te, endTimes[0]]

    elif cnt == result and flag:
        resultTime[1] = tx
print(result)
print(*resultTime)

