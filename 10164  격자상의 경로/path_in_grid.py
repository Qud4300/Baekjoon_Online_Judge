# BOJ 10164 격자상의 경로
from math import factorial
fac = factorial
n, m, k = map(int, input().split())
if k:
    tar = ((k-1)//m, (k-1)%m)
else:
    tar = (0, 0)
remain = (n-1-tar[0], m-1-tar[1])

p1 = fac(sum(tar)) // fac(tar[0]) // fac(tar[1])
p2 = fac(sum(remain)) // fac(remain[0]) // fac(remain[1])

print(p1*p2)
