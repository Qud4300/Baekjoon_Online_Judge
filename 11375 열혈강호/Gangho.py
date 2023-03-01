# BOJ 11375 열혈강호
import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline

n, m = map(int, input().split())
jobs = [[]]+[[*map(int, input().split())][1:] for _ in range(n)]
matched = [0 for _ in range(m+1)]
res = 0


def dfs(a):
    for job in jobs[a]:
        if visited[job]:
            continue
        visited[job] = True
        if matched[job] == 0 or dfs(matched[job]):
            matched[job] = a
            return True
    return False


for i in range(1,n+1):
    visited = [False]*(m+1)
    dfs(i)

print(len(matched)-matched.count(0))