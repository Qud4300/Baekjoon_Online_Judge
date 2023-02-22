# BOJ 2738 행렬덧셈
res = ""
n, m = [*map(int, input().split())]
mat = []
for ROWS in range(n):
    mat.append([*map(int, input().split())])
for i in range(n):
    temp = [*map(int, input().split())]
    for j in range(m):
        mat[i][j] += temp[j]
print('\n'.join([' '.join(map(str, mat[i])) for i in range(n)]))
