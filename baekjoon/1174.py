N = int(input())

result = []
def req(num, now):
    if now != "":
        result.append(int(now))
    for i in range(num-1, -1, -1):
        req(i, now + str(i))

for i in range(10):
    req(i, str(i))
result = list(set(result))
result.sort()
if len(result) <= N-1:
    print(-1)
else:
    print(result[N-1])