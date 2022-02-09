# BOJ 2436 공약수


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
        res.append([i, count])
    if n != 1:
        res.append([n, 1])
    return res


def findMinDiffPair(arr, n):
    stage = [1]
    for i in arr:
        next_stage = set()
        for j in stage:
            next_stage.add(j)
            next_stage.add((i[0]**i[1])*j)
        stage = next_stage
    cur_min = n-1
    res = (1, n)
    for i in stage:
        cur = abs(i-n//i)
        if cur != 0 and cur < cur_min:
            cur_min = cur
            res = (i, n//i)
    return res


g, l = map(int, input().split())
r = l // g if l % g == 0 else None

if r:
    s, p = sorted(findMinDiffPair(factorize(r), r))
    print(s*g, p*g)
