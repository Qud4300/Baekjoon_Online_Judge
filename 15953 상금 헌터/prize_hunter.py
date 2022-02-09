# BOJ 15953 상금 헌터
import sys

input = sys.stdin.readline
n_2017 = [0] + [i for i in range(1, 7) for j in range(i)]
p_2017 = [0, 500, 300, 200, 50, 30, 10]
n_2018 = [0] + [i for i in range(1, 6) for j in range(2**(i-1))]
p_2018 = [0, 512, 256, 128, 64, 32]
for TESTCASE in range(int(input())):
    a, b = map(int, input().split())
    if a > 21:
        a = 0
    if b > 31:
        b = 0
    print((p_2017[n_2017[a]] + p_2018[n_2018[b]]) * 10000)
