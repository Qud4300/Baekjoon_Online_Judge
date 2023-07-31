import sys
input = sys.stdin.readline

def LCA(a, b):
    if level[a] < level[b]:
        a, b = b, a
    
    # 깊이를 맞춰줍니다.
    for i in range(max_height, -1, -1):
        if level[a] - (1 << i) >= level[b]:
            a = table[a][i]
    
    if a == b:
        return str(a)
    
    # 공통 조상을 찾아갑니다.
    for i in range(max_height, -1, -1):
        if table[a][i] != table[b][i]:
            a = table[a][i]
            b = table[b][i]
    
    return str(table[a][0])

def dfs(root):
    stack = [(root, 0, -1)]
    
    while stack:
        x, depth, parent = stack.pop()
        
        if level[x] != -1:
            continue
        
        level[x] = depth
        table[x][0] = parent
        
        for c in edges[x]:
            stack.append((c, depth + 1, x))

if __name__ == '__main__':
    n = int(input())
    edges = [[] for _ in range(n+1)]
    
    for _ in range(n-1):
        a, b = map(int, input().split())
        edges[a].append(b)
        edges[b].append(a)
    
    max_height = (n + 1).bit_length() - 1
    level = [-1] * (n+1)
    table = [[-1] * (max_height+1) for _ in range(n+1)]
    
    dfs(1)
    
    for j in range(1, max_height+1):
        for i in range(1, n+1):
            if table[i][j-1] != -1:
                table[i][j] = table[table[i][j-1]][j-1]
    
    m = int(input())
    query = [list(map(int, input().split())) for _ in range(m)]
    
    result = []
    for x, y in query:
        result.append(LCA(x, y))
    
    print('\n'.join(result))
