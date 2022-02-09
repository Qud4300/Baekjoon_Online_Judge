# BOJ 5348 LCM


def GCD(a,b):
    if b > a:
        a,b = b,a
    while b != 0:
        a = a%b
        a,b = b,a
    return a


def LCM(a,b):
    g = GCD(a,b)
    return a*b//g


for TEST_CASE in range(int(input())):
    A, B = map(int, input().split())
    print(LCM(A,B))
