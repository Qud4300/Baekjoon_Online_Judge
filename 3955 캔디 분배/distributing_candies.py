# BOJ 3955 캔디 분배

import sys
input = sys.stdin.readline


def EEA(a, b):
    k, r0 = a, a
    r1 = b
    s0 = 1
    s1 = 0
    t0 = 0
    t1 = 1
    while r1:
        q = r0//r1
        r = r0%r1
        r0 = r1
        r1 = r
        s = s0 - q*s1
        t = t0 - q*t1
        s0 = s1
        s1 = s
        t0 = t1
        t1 = t
    t0 = (t0 % k + k) % k
    if r0 != 1 or t0 > 10**9:
        return "IMPOSSIBLE"
    else:
        return t0


for TEST_CASE in range(int(input())):
    K, C = map(int, input().split())
    if C == 1:
        if K+1 > 10**9:
            print("IMPOSSIBLE")
        else:
            print(K+1)
    elif K == 1:
        print(1)
    else:
        print(EEA(K, C))
