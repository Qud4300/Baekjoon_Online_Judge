# BOJ 2665 미로만들기
from collections import deque

n = int(input())
arr = [input() for _ in range(n)]
limit = n*n - 2
stage = deque([[0, (0, 0)]])
visited = [[False]*n for _ in range(n)]

while stage:
    cost, loc = stage.popleft()
    for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
        tx, ty = loc[0]+dx, loc[1]+dy
        if tx < 0 or tx > n-1 or ty < 0 or ty > n-1:
            continue
        if visited[loc[0]][loc[1]]:
            continue
        if tx == n-1 and ty == n-1:
            print(cost)
            exit()
        if arr[tx][ty] == '1' and cost < limit:
            stage.appendleft([cost, (tx, ty)])
        elif cost+1 < limit:
            stage.append([cost+1, (tx, ty)])
    visited[loc[0]][loc[1]] = True
