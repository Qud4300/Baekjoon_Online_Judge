# BOJ 5063 TGN
import sys
input = sys.stdin.readline

for TESTCASE in range(int(input())):
    r, e, c = map(int, input().split())
    if e - c > r:
        print("advertise")
    elif e - c == r:
        print("does not matter")
    else:
        print("do not advertise")
