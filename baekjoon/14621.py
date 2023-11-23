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

N, M = map(int, input().split())

school = list(input().split())
school = [0] + school

parent = [0] * (N+1)

for i in range(1, N+1):
    parent[i] = i
edges = []
result = 0
edge_count = 0
for _ in range(M):
    a, b, cost = map(int ,input().split())
    if (school[a] == school[b]):
        continue
    edges.append((cost, a, b))

edges.sort()
for edge in edges:
    cost, a, b = edge

    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        edge_count += 1
        result += cost

if edge_count != N-1:
    result = -1
print(result)
