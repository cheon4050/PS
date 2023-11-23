import sys
input = sys.stdin.readline

N, M, K = map(int, input().split())

stree = [0] * (4*(N+1))

arr = [int(input()) for i in range(N)]

arr = [0] + arr

def merge(left, right):
    return (left * right) % 1000000007

def build(stree, node, left, right):

    if left == right:
        stree[node] = arr[left]
        return stree[node]

    mid = left + (right - left)//2
    left_val = build(stree, 2*node, left, mid)
    right_val = build(stree, 2*node + 1, mid + 1, right)
    stree[node] = merge(left_val, right_val)
    return stree[node]

def query(start, end, node, left, right):

    if end < left or start > right:
        return 1

    if start <= left and right <= end:
        return stree[node]

    mid = left + (right - left) //2
    left_val = query(start, end, 2*node, left, mid)
    right_val = query(start, end, 2*node + 1, mid+1, right)
    return merge(left_val, right_val)

def update(idx, val, node, left, right):
    if idx < left or idx > right:
        return stree[node]

    if left == right:
        stree[node] = val
        return stree[node]

    mid = left + (right - left) //2
    left_val = update(idx, val, 2*node, left, mid)
    right_val = update(idx, val, 2*node+1, mid+1, right)
    stree[node] = merge(left_val, right_val)
    return stree[node]

build(stree, 1, 0, len(arr)-1)

for _ in range(M+K):
    a, b, c = map(int, input().split())
    if a == 1:
        update(b, c, 1, 0, len(arr)-1)
    else:
        print(query(b, c, 1, 0, len(arr)-1))

