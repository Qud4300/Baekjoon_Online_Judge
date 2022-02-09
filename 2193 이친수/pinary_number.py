# BOJ 2193 Pinary number

n = int(input())

dp = [[0] * n for _ in range(2)]
dp[1][0] = 1

for i in range(1, n):
    dp[1][i] = dp[0][i-1]
    dp[0][i] = dp[0][i-1] + dp[1][i-1]
print(dp[1][n-1]+dp[0][n-1])
