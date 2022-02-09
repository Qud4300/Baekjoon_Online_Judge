# BOJ 10253 헨리


def gcd(n, m):
    if m > n:
        n, m = m, n
    while m != 0:
        n = n%m
        n, m = m, n
    return n


def lcm(n, m):
    return n*m//gcd(n, m)


for TEST_CASE in range(int(input())):
    a, b = map(int, input().split())
    while a != 0:
        cur = b//a
        while a*cur < b:
            cur += 1
        l = lcm(cur, b)
        a = a*l//b - l//cur
        g = gcd(a, l)
        a, b = a//g, l//g
    print(cur)