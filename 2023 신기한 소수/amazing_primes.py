# BOJ 2023 신기한 소수

head = [2, 3, 5, 7]
tail = [1, 3, 7, 9]


def sieve(n, m):
    temp = [True for _ in range(m + 1)]
    temp[1] = False
    for i in range(2, int(m**0.5) + 1):
        if temp[i]:
            for j in range(i+i, m + 1, i):
                temp[j] = False
    return [i for i in range(n, m+1) if temp[i]]


def isPrime(arr:list, a:int):
    for i in arr:
        if i > a:
            break
        if a!=i and a%i==0:
            return False
    return True


def gen_prime(n):
    primes = sieve(2, int((10**n)**0.5)+1)
    cur = 1
    stage = head
    while cur < n and stage:
        next_stage = []
        for i in stage:
            for j in tail:
                temp = 10*i+j
                if isPrime(primes, temp):
                    next_stage.append(temp)
        stage = next_stage
        cur += 1
    if cur==n:
        return stage


print('\n'.join(map(str, gen_prime(int(input())))))
