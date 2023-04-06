
N = int(input())

result = []
def req(s, v):
    if v == N:
        result.append(s)
        return
    v += 1
    for i in range(1, 4):
        k = str(i)
        tmp = s + k
        for j in range(1, v//2 +1):

            if tmp[-j:] == tmp[(-j)*2:-j]:
                break
        else:
            req(tmp, v)
            if result:
                return
req("", 0)

print(result[0])