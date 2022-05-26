# BOJ 5719 거의 최단 경로
import sys
import heapq
input = sys.stdin.readline
INF = float("inf")


def dijkstra(n, s):
    stage = [(0, s)]
    visited = [False for _ in range(n)]
    while stage:
        cost, node = heapq.heappop(stage)
        if visited[node]:
            continue
        visited[node] = True
        for i in available[node]:
            if roads[node][i]+cost < path[i]:
                path[i] = roads[node][i] + cost
                if not visited[i]:
                    heapq.heappush(stage, (roads[node][i]+cost, i))
    return


def backtrack():
    stage = [d]
    remove_list = set()
    visited = [False for _ in range(n)]
    while stage:
        next_stage = []
        while stage:
            cur = stage.pop()
            if visited[cur]:
                continue
            visited[cur] = True
            for prev, cost in back[cur]:
                if cost + path[prev] == path[cur]:
                    if not visited[prev]:
                        next_stage.append(prev)
                    if (prev, cur, cost) not in remove_list:
                        remove_list.add((prev, cur, cost))
        stage = next_stage
    return remove_list


while True:
    n, m = map(int, input().split())
    if n==m==0:
        break
    available = [set() for _ in range(n)]
    path = [INF for _ in range(n)]
    back = [set() for _ in range(n)]
    roads = [[INF]*n for _ in range(n)]
    s, d = map(int, input().split())
    for _ in range(m):
        u, v, p = map(int, input().split())
        available[u].add(v)
        roads[u][v] = p
        back[v].add((u, p))
    path[s] = 0
    dijkstra(n, s)
    rm_list = backtrack()
    for u, v, p in rm_list:
        if v in available[u]:
            available[u].remove(v)
            roads[u][v] = INF
            back[v].remove((u,p))
    path = [INF for _ in range(n)]
    dijkstra(n, s)
    res = path[d]
    if res == INF:
        print(-1)
    else:
        print(res)
