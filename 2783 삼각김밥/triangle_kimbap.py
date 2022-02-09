# BOJ 2783 삼각김밥
import sys
input = sys.stdin.readline

a, b = map(int, input().split())
n = int(input())
arr = sorted([[*map(int, input().split())] for _ in range(n)], key = lambda x : x[0]/x[1])

if a/b > arr[0][0]/arr[0][1]:
    print(round(arr[0][0] / arr[0][1] * 1000, 2))
else:
    print(round(a/b * 1000, 2))
