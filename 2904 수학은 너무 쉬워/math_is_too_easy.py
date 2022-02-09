# BOJ 2904 수학은 너무 쉬워
from collections import defaultdict


def sieve(a):
    temp = [True] * (a + 1)
    temp[0], temp[1] = False, False
    for i in range(2, a + 1):
        if temp[i]:
            for j in range(i + i, a + 1, i):
                temp[j] = False
    return temp

def sieve_s(a):
    res = []
    temp = [True] * (a + 1)
    temp[0], temp[1] = False, False
    for i in range(2, a + 1):
        if temp[i]:
            res.append(i)
            for j in range(i + i, a + 1, i):
                temp[j] = False
    return res


primes = sieve(1000000)
primes_s = sieve_s(1000000)


def factorize_cum(a: int, d: defaultdict):
    i = 0
    temp = defaultdict(int)
    bound = a**0.5 + 1
    while primes_s[i] <= bound:
        while a % primes_s[i] == 0:
            d[primes_s[i]] += 1
            temp[primes_s[i]] += 1
            a //= primes_s[i]
        i += 1
    if a != 1:
        d[a] += 1
        temp[a] += 1
    return temp


def GCD(a, b):
    if a < b:
        a, b = b, a
    while b != 0:
        a %= b
        a, b = b, a
    return a


n = int(input())
arr = [*map(int, input().split())]
gcd = 1
fac = []
total = defaultdict(int)
for i in arr:
    fac.append(factorize_cum(i, total))

components = []
for k, v in sorted(total.items(), key=lambda x: x[1], reverse=True):
    if v < n:
        break
    components.append([k,v//n])
    gcd *= k ** (v//n)

count = 0

for fac_i in fac:
    for k, v in components:
        if fac_i[k] < v:
            count += v - fac_i[k]

print(gcd, count)
