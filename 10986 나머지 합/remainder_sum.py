# BOJ 10986 나머지 합

n, m = map(int, input().split())
arr = [0] + [*map(int, input().split())]
res = 0
remains = [0 for i in range(m)]
remains[0] = 1
for i in range(1, n+1):
    arr[i] = (arr[i] + arr[i-1]) % m
    remains[arr[i]] += 1

for r in remains:
    if r>1:
        res += r*(r-1)//2

print(res)
