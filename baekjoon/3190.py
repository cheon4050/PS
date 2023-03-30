from collections import deque
N = int(input())
arr = [[0] * N for i in range(N)]

K = int(input())

for _ in range(K):
    x, y = map(int, input().split())
    arr[x-1][y-1] = 1

L = int(input())

commands = deque([])
for _ in range(L):
    s, command = input().split()
    commands.append([int(s), command])

snake = deque([[0,0]])
direction = 0
move = [(0, 1), (1, 0), (0, -1), (-1, 0)]
result = 1
x, y = 0, 0
i = 0

while True:
    x += move[direction][0]
    y += move[direction][1]
    if 0 <= x < N and 0 <= y < N and [x, y] not in snake:
        result += 1
        snake.appendleft([x, y])
        if not arr[x][y]:
            snake.pop()
        else:
            arr[x][y] = 0
    else:
        print(result)
        break
    i += 1
    if commands:
        if commands[0][0] == i:
            _, command = commands.popleft()
            if command == "D":
                direction = (direction + 1) % 4
            else:
                direction = (direction - 1) % 4
