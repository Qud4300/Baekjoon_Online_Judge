# BOJ 2875 λν or μΈν΄

n, m, k = map(int, input().split())
remains = 0

if 2*m >= n:
    teams = n//2
    remains = m-teams
else:
    teams = m
    remains = n - 2*m
while remains < k:
    teams -= 1
    remains += 3

print(teams)
