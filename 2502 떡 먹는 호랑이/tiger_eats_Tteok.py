# BOJ 2502 떡 먹는 호랑이

arr = [(1,0), (0,1), (1,1)]

d, k = map(int, input().split())
for i in range(3, d):
    arr.append((arr[i-1][0] + arr[i-2][0], arr[i-1][1]+arr[i-2][1]))

A, B = arr[-1]

for a in range(1, k-B):
    for b in range(1, k-A):
        if a*A + b*B == k:
            print(a, b, sep='\n')
            exit()
