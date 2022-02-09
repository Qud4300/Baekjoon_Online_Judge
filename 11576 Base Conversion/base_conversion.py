# BOJ 11576 Base Conversion

A, B = map(int, input().split())
m = int(input())
num = 0
arr = [*map(int, input().split())]
for i in range(m):
    num += arr[i]*(A**(m-i-1))
res = []
start = 24
while B**start > num and start > 0:
    start -= 1
for i in range(start, 0, -1):
    t = B**i
    res.append(num//t)
    num = num%t
res.append(num)
print(*res)
