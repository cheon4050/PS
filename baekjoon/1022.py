r1, c1, r2, c2 = map(int, input().split())

arr = [[0] * (abs(c2-c1)+1) for i in range(abs(r2-r1)+1)]

for i in range(r1, r2+1):
    for j in range(c1, c2+1):
        if abs(i) < abs(j):
            x = (abs(j * 2) + 1) ** 2
            if j > 0:
                arr[i-r1][j-c1] = ((j-1) * 2 + 1)**2 + j - i
            else:
                arr[i-r1][j-c1] = x - abs(j*2) + i + j
        else:
            x = (abs(i * 2) + 1) ** 2
            if i > 0:
                if i == j:
                    arr[i-r1][j-c1] = x
                else:
                    arr[i - r1][j - c1] = x + j - i
            else:
                arr[i - r1][j - c1] = x - abs(i * 2)*3 -i - j

strLen = 0
for i in range(r2-r1+1):
    for j in range(c2-c1+1):
        strLen= max(len(str(arr[i][j])), strLen)

for i in range(r2-r1+1):
    for j in range(c2-c1+1):
        if len(str(arr[i][j])) < strLen:
            for k in range(strLen-len(str(arr[i][j]))):
                print(" ", end ="")
        print(arr[i][j], end= " ")
    print()