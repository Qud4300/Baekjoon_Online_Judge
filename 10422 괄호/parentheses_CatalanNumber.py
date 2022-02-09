# BOJ 10422 괄호
import sys
from math import factorial as fac
input = sys.stdin.readline
A = 1000000007
for TEST_CASE in range(int(input())):
    # Catalan Number, Cat(n) = (2*n)! / n! * (n+1)!
    L = int(input())
    if L%2:
        print(0)
    else:
        n = L//2
        print((fac(2*n)//(fac(n)*fac(n+1)))%A)
