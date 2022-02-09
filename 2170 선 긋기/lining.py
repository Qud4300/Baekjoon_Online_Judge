# BOJ 2170 선 긋기

import sys
input = sys.stdin.readline

n = int(input())
pos = sorted([[*map(int, input().split())] for _ in range(n)], key=lambda x: x[0], reverse=True)
cur = pos.pop()
res = 0
while cur:
    while cur and pos and (cur[0] <= pos[-1][0] <= cur[1]):
        cur[1] = max(cur[1], pos[-1][1])
        pos.pop()
    res += cur[1]-cur[0]
    cur = pos.pop() if pos else None

print(res)