# BOJ 2824 최대공약수
from collections import defaultdict


def primes(a):
    res = []
    arr = [True for _ in range(a + 1)]
    for i in range(2, a + 1):
        if arr[i] is True:
            res.append(i)
            for j in range(i + i, a + 1, i):
                arr[j] = False
    return res


def factorize(a):
    res = defaultdict(int)
    for p in prime:
        while a % p == 0:
            res[p] += 1
            a //= p
    if a != 1:
        res[a] += 1
    return res


def dict_sum(dic_A: dict, dic_B: dict):
    for key, val in dic_B.items():
        dic_A[key] += val
    return dic_A


prime = primes(int(1000000000 ** 0.5))
n = int(input())
A = [*map(int, input().split())]
m = int(input())
B = [*map(int, input().split())]

factors_A = defaultdict(int)
factors_B = defaultdict(int)
for a in A:
    factors_A = dict_sum(factors_A, factorize(a))
for b in B:
    factors_B = dict_sum(factors_B, factorize(b))
res = 1
for i in set(factors_A.keys()).intersection(set(factors_B.keys())):
    res *= i**min(factors_A[i], factors_B[i])

print(str(res)[-9:])
