# BOJ 2745 진법 변환

def conversion(a):
    if a in '0123456789':
        return int(a)
    else:
        return ord(a)-55


n, b = input().split()
b = int(b)
res = 0
digit = 1
for i in reversed(n):
    res += digit * conversion(i)
    digit *= b

print(res)
