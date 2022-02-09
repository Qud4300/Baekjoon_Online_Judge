# BOJ 14490 백대열

def GCD(a, b):
    if b > a:
        a, b = b, a
    while b != 0:
        a = a % b
        a, b = b, a
    return a


n, m = map(int, input().split(':'))
g = GCD(n, m)
print(n // g, ':', m // g, sep='')
