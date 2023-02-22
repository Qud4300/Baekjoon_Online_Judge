# # BOJ 2566 최댓값
mat = []
for ROW in range(9):
    mat.append([*map(int, input().split())])
M = 0
coord = (0,0)
flag = False
for i in range(9):
    for j in range(9):
        if M<mat[i][j]:
            M = mat[i][j]
            coord = (i,j)
        if M == 100:
            print(f'{M}\n{i} {j}')
            flag = True
            break
    if flag: break
if not flag:
    print(f'{M}\n{coord[0]+1} {coord[1]+1}')