# BOJ 2563 색종이
arr = [[False]*100 for _ in range(100)]
n = int(input())
coords = [[*map(int,input().split())] for _ in range(n)]
for a, b in coords:
    for i in range(a, a+10):
        for j in range(b, b+10):
            arr[i][j] = True
print(sum(map(sum, arr)))