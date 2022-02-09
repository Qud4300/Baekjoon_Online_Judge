# BOJ 2407 조합
from math import factorial

n, m = map(int, input().split())

print(factorial(n)//factorial(n-m)//factorial(m))
