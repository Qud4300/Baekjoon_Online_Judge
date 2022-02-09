# BOJ 1256 사전

n, m, k = map(int, input().split())
dp = [[1]*(m+1) for _ in range(n+1)]  # dp[n][m]
dp[0][0] = 0
for i in range(1, n+1):
    for j in range(1, m+1):
        dp[i][j] = dp[i-1][j] + dp[i][j-1]

if dp[n][m] < k:
    print(-1)
else:
    res = ""
    a, b = n, m
    while True:
        if a==0:
            res += 'z'*b
            break
        elif b==0:
            res += 'a'*a
            break
        else:
            if dp[a-1][b] >= k:  # if the size of placing-'a' case can cover remaining k-cases,
                res += 'a'  # place 'a' and continue.
                a -= 1
            else:  # if placing 'a' cannot cover k-cases,
                res += 'z'  # place 'z' and subtract the size of placing-'a' case, which is not considered.
                k -= dp[a-1][b]  # then we just can consider remaining cases(the subtracted) from placing-'z' cases. 
                b -= 1
    print(res)
