from itertools import combinations

N, K = map(int, input().split())

arr = []

spelling = ["a", "n", "t", "i", "c"]
ABCDEFG = ["b", "d", "e", "f", "g", "h", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "u", "v", "w", "x", "y", "z"]
maxCnt = 0
for _ in range(N):
    arr.append(input()[4:-4])

if K < 5:
    print(0)
else:
    for combi in combinations(ABCDEFG, K-5):
        cnt = 0
        spellingArr = spelling + list(combi)
        for s in arr:
            for c in s:
                if not c in spellingArr:
                    break
            else:
                cnt += 1
        maxCnt = max(cnt, maxCnt)
    print(maxCnt)