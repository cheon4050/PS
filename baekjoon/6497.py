import sys

input = sys.stdin.readline

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b
m, n = map(int, input().split())
while (not (m == 0 and n == 0)):
    edges = []
    parent = [0] * (m)
    total_cost = 0
    for i in range(m):
        parent[i] = i

    for _ in range(n):
        a, b, cost = map(int, input().split())
        total_cost += cost
        edges.append((cost, a, b))

    edges.sort()

    result = 0

    for edge in edges:
        cost, a, b = edge
        if find_parent(parent, a) != find_parent(parent, b):
            union_parent(parent, a, b)
            result += cost

    print(total_cost - result)
    m, n = map(int, input().split())