# BOJ 1915 가장 큰 정사각형

n, m = map(int, input().split())
arr = [[int(i) for i in input()] for _ in range(n)]
res = max([arr[i][0] for i in range(n)]+[arr[0][j] for j in range(m)])

for i in range(1, n):
    for j in range(1, m):
        arr[i][j] = min(arr[i-1][j-1], arr[i][j-1], arr[i-1][j])*arr[i][j] + arr[i][j]
        if res < arr[i][j]:
            res = arr[i][j]

print(res**2)
