N = int(input())

arr = []
for i in range(N):
    arr.append(list(map(int, input().split())))

numList = [arr[0][0]]
for i in range(N):
    numList.append(arr[i][1])

def req(start, end, arr):
    if not arr:
        return 0
    minNum = min(arr)
    cnt = start * end * minNum
    minNumIndex = arr.index(minNum)
    cnt += req(start, minNum, arr[:minNumIndex])
    cnt += req(minNum, end, arr[minNumIndex+1:])
    return cnt

print(req(numList[0], numList[-1], numList[1:-1]))







# INF = int(1e9)
# dpArr = [[0] * (N) for i in range(N)]
# print(dpArr)




# def dp(index, visited, arr, cnt):
#     if cnt == N:
#
#         return arr[i][]
#
#     cost = INF
#     for i in range(N):
#         if not visited[i]:
#             visited[i] = True
#             cost = min(cost, dp(i, visited[:], arr, cnt+1))
#             visited[i] = False
#     dp[cnt][visited] = cost
#     return dp[cnt][visited]
#


# numList = [arr[0][0]]
# for i in range(N):
#     numList.append(arr[i][1])
#
#
# sum = 0
# for i in range(N-1):
#     maxNum = max(numList[1:-1])
#     print(numList[1:-1])
#     maxNumIndex =numList.index(maxNum)
#     print(maxNumIndex)
#     sum += numList[maxNumIndex-1] * numList[maxNumIndex+1] * numList[maxNumIndex]
#     numList.pop(maxNumIndex)
# print(sum)