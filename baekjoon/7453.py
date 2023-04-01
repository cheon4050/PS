import sys
input = sys.stdin.readline

N = int(input())
A, B, C, D = [], [], [], []
for i in range(N):
    a, b, c, d = map(int,input().split())
    A.append(a)
    B.append(b)
    C.append(c)
    D.append(d)

arr = []
arr2 = []

for i in range(N):
    for j in range(N):
        arr.append(A[i]+B[j])
        arr2.append(C[i]+D[j])

arr.sort()
arr2.sort()


left = 0
right = len(arr2)-1
result = 0
maxLen = N**2

while left < maxLen and right >= 0:
    x = arr[left] + arr2[right]
    if x < 0:
        left += 1
    elif x > 0:
        right -= 1
    else:
        cnt1 = 1
        while left + 1 < maxLen and arr[left+1] == arr[left]:
            cnt1 += 1
            left += 1
        left += 1
        cnt2 = 1
        while right - 1 >= 0 and arr2[right-1] == arr2[right]:
            cnt2 += 1
            right -= 1
        right -= 1
        result += cnt1 * cnt2


print(result)