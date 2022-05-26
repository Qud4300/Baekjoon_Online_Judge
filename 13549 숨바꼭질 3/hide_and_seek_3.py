# BOJ 13549 숨바꼭질 3
import sys
import math
import heapq
input = sys.stdin.readline
INF = float("INF")
time = [INF for _ in range(100001)]
n, k = map(int, input().split())
if k == 0 or k==n or k < n:
    print(n-k)
    exit()

queue = [(0, n)]
visited = [False for _ in range(100001)]
time[n] = 0
visited[n] = True
while queue:
    t, loc = heapq.heappop(queue)
    for c, i in ((0, 2*loc), (1, loc-1), (1, loc+1)):
        if i<0 or i>100000 or visited[i]: continue
        temp = t + c
        if i == k:
            print(temp)
            exit()
        time[i] = temp
        heapq.heappush(queue, [temp, i])
        visited[i] = True
