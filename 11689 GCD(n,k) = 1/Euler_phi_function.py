# BOJ 11689 GCD(n,k) = 1

n = int(input())
factors = []
for i in range(2, int(n**0.5)+1):
    count = 0
    while n%i == 0:
        n //= i
        count += 1
    if count:
        factors.append([i, count])
    if n == 1:
        break
if n != 1:
    factors.append([n, 1])

phi = 1
for i, count in factors:
    phi *= (i-1)*i**(count-1)

print(phi)