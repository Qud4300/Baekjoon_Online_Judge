# 11377 열혈강호 3
import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline

def dfs(a):
    if not visited[a]:
        visited[a] = True
        for job in jobs[a]:
            if matched[job] == a:
                continue
            if matched[job] == 0 or dfs(matched[job]):
                matched[job] = a
                return True
    return False


if __name__ == "__main__":
    n, m, k = map(int, input().split())
    jobs = [[]] + [[*map(int,input().split())][1:] for _ in range(n)]
    matched = [0 for _ in range(m+1)]
    res = 0

    for i in range(1,n+1):
        visited = [False]*(n+1)
        if dfs(i):
            res += 1
    # another k-number of matching.
    for i in range(1,n+1):
        visited = [False]*(n+1)
        if dfs(i):
            res += 1
            k -= 1
            if k == 0:
                break
        
    print(res)