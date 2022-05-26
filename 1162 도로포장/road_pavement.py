# BOJ 1162 도로포장
import sys
import heapq
input = sys.stdin.readline
INF = float('inf')

n, m, k = map(int, input().split())
path = [[INF]*(k+1) for _ in range(n+1)]
available = [[] for _ in range(n+1)]
for u, v, c in [[*map(int, input().split())] for _ in range(m)]:
    available[u].append([v, c])
    available[v].append([u, c])

path[1] = [0]*(k+1)
stage = [(0, 1, k)]
while stage:
    cost, cur, chance = heapq.heappop(stage)
    if path[cur][chance] < cost:
        continue
    for i, c in available[cur]:
        if path[i][chance] > cost + c:
            path[i][chance] = cost + c
            heapq.heappush(stage, (cost+c, i, chance))
        if chance and path[i][chance-1] > cost:
            path[i][chance-1] = cost
            heapq.heappush(stage, (cost, i, chance-1))

print(min(path[-1]))
