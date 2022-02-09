# BOJ 1026 보물

n = int(input())
A = sorted([*map(int, input().split())], reverse=True)
B = [*map(int, input().split())]
S = 0
while A:
    cur_max = 0
    for i in range(len(B)):
        if B[i] > cur_max:
            cur_max = B[i]
    S += A.pop() * cur_max
    B.remove(cur_max)

print(S)
