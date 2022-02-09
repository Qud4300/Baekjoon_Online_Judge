# BOJ 1188 음식 평론가


def gcd(a,b):
    if b>a:
        a,b = b,a
    while b!=0:
        a = a%b
        a,b = b,a
    return a

n, m = map(int, input().split())

print(m - gcd(n, m))
