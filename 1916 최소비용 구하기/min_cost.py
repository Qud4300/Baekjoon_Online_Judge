# BOJ 1916  최소비용 구하기
import sys
import heapq
input = sys.stdin.readline

INF = float("INF")
n = int(input())
m = int(input())
edges = [[] for _ in range(n + 1)]
path = [INF for _ in range(n+1)]
for _ in range(m):
    s, d, c = map(int, input().split())
    edges[s].append([c, d])
d, a = map(int, input().split())
stage = [(0, d)]
visited = [False for _ in range(n+1)]
while stage:
    cost, node = heapq.heappop(stage)
    if node == a:
        break
    if visited[node]:
        continue
    for c, dest in edges[node]:
        if path[dest] > cost + c:
            path[dest] = cost + c
            if not visited[dest]:
                heapq.heappush(stage, (path[dest], dest))
    visited[node] = True

print(path[a])
