# BOJ 2089 -2진수

def r2(n):
    if n==0:
        return '0'
    res = ''
    while n != 1:
        res = str(n % 2) + res
        if n % 2:
            n -= 1
        n //= -2
    res = '1' + res
    return res


print(''.join(r2(int(input()))))
