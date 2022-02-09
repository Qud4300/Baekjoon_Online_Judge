# BOJ 1049 기타줄
import sys, math
input = sys.stdin.readline

n, m = map(int, input().split())
min_package, min_indiv = 1000, 1000
for _ in range(m):
    pack, string = map(int, input().split())
    min_package = min(min_package, pack)
    min_indiv = min(min_indiv, string)

if min_indiv * 6 < min_package:
    print(n*min_indiv)
elif n%6 * min_indiv > min_package:
    print(math.ceil(n/6) * min_package)
else:
    print((n//6)*min_package + (n % 6)*min_indiv)

