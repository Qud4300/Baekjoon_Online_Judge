# BOJ 11812 K진트리
import math
import sys
input = sys.stdin.readline

N, K, Q = map(int, input().split())


def parent(a):
    if a > 1:
        return (a-2)//K + 1
    return 1


def level(a):
    temp = 0
    e = 0
    while temp < a:
        temp += K ** e
        e += 1
    return e


def dist(a, b):
    res = 0
    while level(a) != level(b):
        if level(a) > level(b):
            a = parent(a)
        else:
            b = parent(b)
        res += 1
    while a != b:
        a = parent(a)
        b = parent(b)
        res += 2
    return res


for _ in range(Q):
    A, B = map(int, input().split())
    if K == 1:
        print(abs(A-B))
    else:
        print(dist(A, B))