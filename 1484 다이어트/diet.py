# BOJ 1484 다이어트

g = int(input())
res = []
i = int(g**0.5)+1
while i**2 - (i-1)**2 <= g:
    s, e = 1, i-1
    while e > s:
        m = (s+e)//2
        temp = i ** 2 - m ** 2
        if temp == g:
            e = m
            break
        elif temp > g:
            s = m+1
        else:
            e = m
    if i**2 - e**2 == g:
        res.append(i)
    i += 1

if res:
    print('\n'.join(map(str, res)))
else:
    print(-1)
