# BOJ 11659 구간 합 구하기 4
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
nums = [0]+[*map(int, input().split())]
ranges = [[*map(int, input().split())] for _ in range(m)]
res = ''

p_sum = [0 for _ in range(n+1)]
for i in range(1, n+1):
    p_sum[i] = p_sum[i-1] + nums[i]

for a, b in ranges:
    res += str(p_sum[b] - p_sum[a-1]) + '\n'

print(res.rstrip())
