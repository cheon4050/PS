import sys
from math import ceil, log2
input = sys.stdin.readline

N, M = map(int, input().split())
arr = []

for i in range(N):
    arr.append(int(input()))


height = ceil(log2(N))
tree_size = 1 << (height+1)
tree = [[0, 0] for i in range(tree_size)]

def build(node, start, end):

    if start == end:
        tree[node] = [arr[start], arr[start]]
        return
    mid = (start + end) // 2

    build(node*2, start, mid)

    build(node*2+1, mid+1, end)
    tree[node] = [min(tree[node*2][0], tree[node*2+1][0]), max(tree[node*2][1], tree[node*2+1][1])]

def query(node, start, end, left, right):
    if right < start or end < left:
        return [1000000000, 0]
    if left <= start and end <= right:
        return tree[node]

    mid = (start + end)//2
    left_child = query(node*2, start, mid, left, right)
    right_child = query(node*2+1, mid+1, end, left, right)

    return [min(left_child[0], right_child[0]), max(left_child[1], right_child[1])]

build(1, 0, N-1)
for _ in range(M):
    a, b = map(int, input().split())
    print(*query(1, 0, N-1, a-1, b-1))

