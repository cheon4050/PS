s = input().rstrip()

stack = []
result = []
check = [0] * len(s)
for i in range(len(s)):
    if s[i] == "(":
        stack.append(i)
    elif s[i] == ")":
        a = stack.pop()
        check[i] = a
        check[a] = i

def req(nowString, i, stack):
    if len(s) == i:
        if not stack:
            if s == nowString:
                return
            result.append(nowString)
        return
    if s[i] == "(":
        req(nowString, i + 1, stack[:])
        req(nowString + s[i], i + 1, stack + [i])
    elif s[i] == ")":
        req(nowString, i + 1, stack[:])
        if stack and stack[-1] == check[i]:
            req(nowString + s[i], i + 1, stack[:-1])
    else:
        req(nowString + s[i], i+1, stack[:])

req("", 0, [])
result = sorted(list(set(result)))
for s in result:
    print(s)
