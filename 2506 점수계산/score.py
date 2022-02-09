# BOJ 2506 점수계산

n = int(input())
res = 0
count = 1
for i in [*map(int, input().split())]:
    if i == 1:
        res += count
        count += 1
    else:
        count = 1
print(res)
