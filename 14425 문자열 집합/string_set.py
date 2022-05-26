# BOJ 14425 문자열 집합
import sys
input = sys.stdin.readline

n, m = map(int, input().split())

S = set(input().rstrip() for _ in range(n))
count = 0
for _ in range(m):
    a = input().rstrip()
    if a in S: count += 1
    
print(count)