# BOJ 9085 더하기
import sys
input = sys.stdin.readline

for TEST_CASE in range(int(input())):
    input()
    print(sum([*map(int, input().split())]))
