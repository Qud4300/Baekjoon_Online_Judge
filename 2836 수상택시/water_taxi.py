# BOJ 2836 수상 택시
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = sorted([a for a in [[*map(int, input().split())] for _ in range(n)] if a[1] < a[0]], key=lambda x:(x[0],x[1]))
cur = arr.pop() if arr else None
res = m
while arr and cur:
    if cur[0] >= arr[-1][0] >= cur[1]:
        cur[1] = min(cur[1], arr[-1][1])
        arr.pop()
    else:
        res += (cur[0]-cur[1])*2
        cur = arr.pop()
if cur:
    res += (cur[0]-cur[1])*2
print(res)
