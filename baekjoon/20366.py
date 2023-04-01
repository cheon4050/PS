N = int(input())

arr = list(map(int,input().split()))

arr.sort(reverse=True)

result = 1000000000
for i in range(N):
    for j in range(i+3, N):
        left, right = i+1, j-1
        while left < right:
            x = arr[i] + arr[j] - arr[left] - arr[right]
            if x > 0:
                left += 1
            else:
                right -= 1
            result = min(result, abs(x))
print(result)

# arr.sort(reverse=True)
# result = 1000000000
# for i in range(N):
#     for j in range(i+1, N):
#         for x in range(j+1, N):
#             for y in range(x+1, N):
#                 result = min(result, abs(arr[i]+arr[y]-(arr[j]+arr[x])))
#
# print(result)

