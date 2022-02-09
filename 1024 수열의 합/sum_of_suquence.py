# BOJ 1024 수열의 합

N, L = map(int, input().split())
cur = L
base = L * (L - 1) // 2  # [0 ~ L-1]

while cur < 101:
    if base <= N and (N - base) % cur == 0:
        start = (N - base) // cur
        print(*[i for i in range(start, start + cur)])
        break
    else:
        base += cur
        cur += 1

if cur > 100:
    print(-1)
