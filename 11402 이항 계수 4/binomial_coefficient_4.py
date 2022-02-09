# BOJ 11402 이항 계수 4
import sys
sys.setrecursionlimit(10000)

n, k, m = map(int, input().split())
factorial = [1] * (m + 1)


def pow(a, b, c):
    if b == 1:
        return a
    pow_half = pow(a, b // 2, c)
    if b % 2 == 0:
        return (pow_half ** 2) % c
    else:
        return (pow_half ** 2 * a) % c


def inverse(a):
    # Fermat's little theorem
    # for a and p (not divisible by each other, P is prime number)
    # (a^p)% = p, and (a^p-1)%p = 1
    # then, (a^p-1) as A and 'p-modulo' for inverse of A is, A/p = a^p-2
    return pow(factorial[a], m - 2, m)


for i in range(2, m + 1):
    factorial[i] = (factorial[i - 1] * i) % m

res = 1

while n != 0 and k != 0:
    n_digit = n % m
    n //= m
    k_digit = k % m
    k //= m
    if n_digit < k_digit:
        res = 0
        break
    elif n_digit == k_digit:
        continue
    else:
        res *= factorial[n_digit] * inverse(n_digit - k_digit) * inverse(k_digit)
        res %= m

print(res)
