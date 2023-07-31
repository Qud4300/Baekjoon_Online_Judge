import sys
input = sys.stdin.readline

n = int(input())
a = [*map(int, input().split())]

# table[i][j]에 i번째 숫자에 함수를 2^j번째 적용한 결과를 저장한다.(j = 1,2,4,8,...)
table = [[0] * 19 for _ in range(n)]

# table[x][0] 을 f 함수로 초기화. [0]부터 사용. (즉, f(1)==table[0][0], f^2(3)==table[3][1]
for i in range(n):
    table[i][0] = a[i]

for j in range(1, 19):
    for i in range(n):
        # table[i][0]부터 사용하므로 f2(x)==table[x][1]부터 시작.
        # f^j+1(i+1) = f^j(f^j(i+1)-1)
        table[i][j] = table[table[i][j-1]-1][j-1]

# Query start.
for _ in range(int(input())):
    i, x = map(int, input().split())
    k = 0
    while (1 << k) < i: # 2^k < i
        k += 1

    # i번 적용한 결과에서 x번째 값을 구한다.
    for j in range(k, -1, -1):
        pow = 1<<j
        if pow <= i:
            x = table[x-1][j]
            i -= pow

    print(x)
