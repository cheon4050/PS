from heapq import heappush, heappop
import sys
input = sys.stdin.readline
N, L = map(int, input().split())
arr = list(map(int, input().split()))

q = []
for i in range(N):
    heappush(q, (arr[i], i))

    while q[0][1] <= i-L:
        heappop(q)
    print(q[0][0], end= " ")