# BOJ 2213 트리의 독립집합 - DP, DFS
import sys
input = sys.stdin.readline

n = int(input())
vertice = [0] + [*map(int, input().split())]
edge = [[] for _ in range(n+1)]
visited = [False]*(n+1)
dp = [[0, vertice[i]] for i in range(n+1)]
select = [[] for _ in range(n+1)]
for a,b in [[*map(int, line.split())] for line in sys.stdin.readlines()]:
    edge[a].append(b)
    edge[b].append(a)

def dfs(prev, cur):
    visited[cur] = True
    for node in edge[cur]:
        if not visited[node]:
            dfs(cur, node)
            idx = max([0, 1], key = lambda i: dp[node][i])
            select[cur].append([node, idx])
            dp[cur][0] += dp[node][idx]
            dp[cur][1] += dp[node][0]
    return


dfs(0, 1)
res = [0,[]]
stage = []
if dp[1][0] > dp[1][1]:
    res[0] = dp[1][0] 
    stage.append([1,0])
else :
    res[0] = dp[1][1]
    stage.append([1,1])

visited = [False]*(n+1)
visited[1] = True
while stage:
    next_stage = []
    while stage:
        cur, sel = stage.pop()
        visited[cur] = True
        if sel:
            res[1].append(cur)
            next_stage += [[c, 0] for c in edge[cur] if not visited[c]]
        else:
            next_stage += select[cur]
    stage = next_stage

print(res[0])
print(*sorted(res[1]))

