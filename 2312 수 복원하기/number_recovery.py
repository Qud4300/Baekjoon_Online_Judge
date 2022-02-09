# BOJ 2312 수 복원하기
import sys
input = sys.stdin.readline


def sieve(a, b):
    temp = [True for _ in range(b + 1)]
    for i in range(2, b + 1):
        if temp[i]:
            for j in range(i + i, b + 1, i):
                temp[j] = False
    return [i for i in range(a, b + 1) if temp[i]]


def factorize(n):
    primes = sieve(2, int(n ** 0.5) + 1)
    res = []
    for i in primes:
        count = 0
        while n % i == 0:
            count += 1
            n //= i
        if count:
            res.append([i, count])
    if n != 1:
        res.append([n, 1])
    return res


for TEST_CASE in range(int(input())):
    for a, b in factorize(int(input())):
        print(a,b)

