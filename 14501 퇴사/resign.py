# BOJ 14501 퇴사
import sys
input = sys.stdin.readline

time = []
price = []
dp = []
n = int(input())

for _ in range(n):
    a, b = map(int, input().split())
    time.append(a)
    price.append(b)
    dp.append(b)

dp.append(0)

for i in range(n-1, -1, -1):
    if time[i] + i > n:
        dp[i] = dp[i+1]
    else:
        dp[i] = max(dp[i+1], price[i]+dp[i + time[i]])

print(dp[0])
