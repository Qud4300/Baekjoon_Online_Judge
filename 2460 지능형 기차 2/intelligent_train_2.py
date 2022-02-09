# BOJ 2460 지능형 기차 2

max_passengers = 0
cur = 0
for _ in range(10):
    o, i = map(int, input().split())
    cur = cur - o + i
    max_passengers = max(max_passengers, cur)
print(max_passengers)
