N = int(input())

arr = list(map(int,input().split()))

K = int(input())

kArr = list(map(int,input().split()))


dp = [[0] * (N * 500+1) for i in range(N+1)]


def cal(num, weight):
    if num > N:
        return
    if dp[num][weight]:
        return

    dp[num][weight] = 1

    cal(num+1, weight)
    cal(num+1, weight+arr[num-1])
    cal(num+1, abs(weight-arr[num-1]))

cal(0, 0)

result = []
for i in kArr:
    if i > 15000:
        result.append("N")
        continue
    if dp[N][i] == 1:
        result.append("Y")
    else:
        result.append("N")
print(*result)