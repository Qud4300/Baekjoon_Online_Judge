# BOJ 15897 잘못 구현한 에라토스테네스의 체

n = int(input())
res = n
i = 2
while i < n:
    k = (n-1)//i
    j = (n-1)//k
    res += (k+1)*(j-i+1)
    i = j+1
if i==n:
    res += 1

print(res)
