# BOJ 1238 파티
import sys
import heapq

input = sys.stdin.readline

INF = float("INF")

n, m, x = map(int, input().split())
edges = [[] for _ in range(n + 1)]
path = [[INF for _ in range(n + 1)] for __ in range(n + 1)]
res = [0 for _ in range(n + 1)]

for _ in range(m):
    s, d, t = map(int, input().split())
    edges[s].append([t, d])

for i in range(1, n + 1):
    queue = [(0, i)]
    visited = [False for _ in range(n + 1)]
    while queue:
        cost, node = heapq.heappop(queue)
        if i != x and node == x:
            break
        for c, j in edges[node]:
            temp = cost + c
            if path[i][j] > temp:
                path[i][j] = temp
            if not visited[j]:
                heapq.heappush(queue, (temp, j))
        visited[node] = True
    if i != x:
        res[i] += path[i][x]
    else:
        for j in range(1, n + 1):
            if j == x: continue
            res[j] += path[x][j]

print(max(res))
