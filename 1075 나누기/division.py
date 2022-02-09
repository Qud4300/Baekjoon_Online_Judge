# BOJ 1075 Division

n = int(input())
f = int(input())
arr = []
r = n % f
h = n % 100
cur = h + f - r
while 0 <= cur - f:
    cur -= f
print("%.2d" % cur)
