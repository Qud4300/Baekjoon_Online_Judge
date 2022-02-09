# BOJ 1850 최대공약수

def GCD(a, b):
    if b<a: a,b = b,a
    while b!=0:
        a = a % b
        a, b = b, a
    return a

A, B = map(int, input().split())
print('1'*GCD(A, B))
