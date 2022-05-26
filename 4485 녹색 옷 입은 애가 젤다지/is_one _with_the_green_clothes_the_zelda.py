# BOJ 4485 녹색 옷 입은 애가 젤다지?
import sys
import heapq

input = sys.stdin.readline

n = int(input())
count = 1
while 0 != n:
    arr = [[*map(int, input().split())] for _ in range(n)]
    queue = [[arr[0][0], (0, 0)]]
    path = [[float("INF")] * n for _ in range(n)]
    path[0][0] = arr[0][0]
    visited = [[False] * n for _ in range(n)]
    while queue:
        cost, loc = heapq.heappop(queue)
        x, y = loc[0], loc[1]
        for a, b in [[x + 1, y], [x, y + 1], [x, y - 1], [x - 1, y]]:
            if -1 < a < n and -1 < b < n:
                if not visited[a][b] and path[a][b] > cost + arr[a][b]:
                    heapq.heappush(queue, [cost + arr[a][b], (a, b)])
                    path[a][b] = cost + arr[a][b]
        visited[x][y] = True
    print(f'Problem {count}: {path[-1][-1]}')
    n = int(input())
    count += 1
