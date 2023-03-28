# BOJ 11376 열혈강호
import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline

n, m = map(int, input().split())
jobs = [[]] + [[*map(int,input().split())][1:] for _ in range(n)]
matched = [0 for _ in range(m+1)]
res = 0


def dfs(tup):
    a, b = tup
    if not visited[a]:
        visited[a] = True
        for job in jobs[a]:
            if matched[job] == a:
                continue
            if matched[job] == 0 or dfs(matched[job]):
                matched[job] = (a,b)
                return True
    return False


for i in range(1,n+1):
    for j in (0,1):
        visited = [False]*(n+1)
        if dfs((i,j)):
            res += 1
        
print(res)