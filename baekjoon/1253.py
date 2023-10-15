from collections import defaultdict

N = int(input())

arr = list(map(int, input().split()))
dict = defaultdict(int)
for i in arr:
    dict[i] += 1
numList = []
for i in range(len(arr)):
    for j in range(i+1, len(arr)):
        if (arr[i] == 0 and dict[arr[j]] <= 1) or (arr[j] == 0 and dict[arr[i]] <= 1):
            continue
        elif arr[i] == 0 and arr[j] == 0 and dict[0] <=2:
            continue
        numList.append(arr[i] + arr[j])
numList = list(set(numList))
numList.sort()
result = 0
for num in arr:
    start = 0
    end = len(numList)-1
    while start <= end:
        mid = (start+end) // 2
        if numList[mid] == num:
            result += 1
            break
        if numList[mid] < num:
            start = mid+1
        if numList[mid] > num:
            end = mid-1

print(result)
