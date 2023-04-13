N = int(input())
arr = list(map(str, input().split()))

def check(a, b):
    if int(a+b) >= int(b+a):
        return True
    return False
for i in range(N):
    max_index = i
    for j in range(i+1, N):
        if not check(arr[max_index], arr[j]):
            max_index = j
    arr[i], arr[max_index] = arr[max_index], arr[i]

result = ""
for i in range(N):
    for c in arr[i]:
        if c == "N":
            break
        result+=c
if int(result) == 0:
    result = "0"
print(result)
