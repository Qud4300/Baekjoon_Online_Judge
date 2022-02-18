# BOJ 1764 듣보잡
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
not_heard = set(input()[:-1] for _ in range(n))
not_seen = set(input()[:-1] for _ in range(m))
inter = not_seen.intersection(not_heard)
print(len(inter))
print(*sorted(list(inter)))
