# BOJ 11005 진법 변환 2
import math


def alpha(a):
    if a<10:
        return str(a)
    else:
        return chr(a+55)


n, b = map(int, input().split())
res = ''
s = int(math.log(n, b))
if s==0 or n==0:
    print(alpha(n))
else:
    while s>-1:
        temp = n//(b**s)
        res += alpha(temp)
        n -= temp * b**s
        s -= 1
    print(res)
