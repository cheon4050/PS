import sys
input = sys.stdin.readline

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a< b:
        parent[b] = a
    else:
        parent[a] = b

v, e = map(int, input().split())
parent = [0] * (v+1)
nodeList = []
edges = []
for i in range(v):
    nodeList.append(list(map(int, input().split())))

for i in range(1, v+1):
    parent[i] = i

for i in range(e):
    a, b = map(int, input().split())
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
for i in range(v):
    for j in range(i+1, v):
        cost = (((abs(nodeList[i][0] - nodeList[j][0])) ** 2) + ((abs(nodeList[i][1] - nodeList[j][1]))** 2)) ** (1/2)
        edges.append((cost, i+1, j+1))


result = 0

edges.sort()
cnt = 0
for edge in edges:
    cost, a, b= edge
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        cnt += 1
        result += cost

print("{:.2f}".format(result))

