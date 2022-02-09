# BOJ 17087 숨바꼭질 6

def gcd(a,b):
    if b>a:
        a,b = b,a
    while b!=0:
        a = a%b
        a,b = b,a
    return a


n, s = map(int, input().split())
arr = [*map(lambda x: abs(int(x)-s), input().split())]
g = arr.pop()
while len(arr):
    g = gcd(g, arr.pop())
    if g==1:
        break

print(g)
