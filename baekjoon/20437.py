from collections import defaultdict

T = int(input())

for _ in range(T):
    W = input()
    K = int(input())
    alphabetDict = defaultdict(list)
    minLen = 100000
    maxLen = 0
    for i in range(len(W)):
        alphabetDict[W[i]].append(i)
    for alphabet in alphabetDict:
        if len(alphabetDict[alphabet]) < K:
            continue
        for j in range(len(alphabetDict[alphabet])-K+1):
            x = alphabetDict[alphabet][j+K-1] - alphabetDict[alphabet][j]+1
            minLen = min(minLen, x)
            maxLen = max(maxLen, x)
    if maxLen == 0:
        print(-1)
    else:
        print(minLen, maxLen)


