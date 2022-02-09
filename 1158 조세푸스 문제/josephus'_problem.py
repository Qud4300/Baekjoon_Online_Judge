# BOJ 1158 Josephus' Problem

n, k = map(int, input().split())
v = 0
arr = [str(i) for i in range(1, n+1)]
res = []
while len(arr):
    v = (v+k-1) % len(arr)
    res.append(arr.pop(v))

print('<', ', '.join(res), '>', sep='')
