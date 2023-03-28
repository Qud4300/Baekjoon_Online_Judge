# BOJ 3584 가장 가까운 공통 조상
import sys
input = sys.stdin.readline

res = ''
for TEST_CASE in range(int(input())):
    n = int(input())
    parent = [0]*(n+1)
    visited = [False]*(n+1)
    for _ in range(n-1):
        a, b = map(int, input().split())
        parent[b] = a
    x, y = map(int,input().split())
    while x != 0 or y != 0:
        if x!=0:
            if visited[x]:
                res += str(x)+'\n'
                break
            visited[x] = True
            x = parent[x]
        if y!=0:
            if visited[y]:
                res += str(y)+'\n'
                break
            visited[y] = True
            y = parent[y]
print(res.rstrip())
