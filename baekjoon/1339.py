from collections import defaultdict
N = int(input())
arr = []
for i in range(N):
    arr.append(input())

ddict = defaultdict(int)

for s in arr:
    cnt = 1
    for i in range(len(s)-1, -1, -1):
        ddict[s[i]] += cnt
        cnt *= 10

numArr = list(ddict.items())
numArr.sort(key = lambda x : -x[1])

numDict = {}
NUMBERS = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

for key, _ in numArr:
    numDict[key] = NUMBERS.pop()

def cal(numDict):
    numArr = []
    for s in arr:
        changeString = ""
        for i in range(len(s)):
            changeString += str(numDict[s[i]])
        numArr.append(int(changeString))
    return sum(numArr)

print(cal(numDict))
