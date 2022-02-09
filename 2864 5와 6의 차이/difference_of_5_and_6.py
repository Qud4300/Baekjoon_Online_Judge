# BOJ 2864 5와 6의 차이

M, m = 0, 0
for num in input().split():
    m += int(num.replace('6','5'))
    M += int(num.replace('5','6'))

print(m, M)
