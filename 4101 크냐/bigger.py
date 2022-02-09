# BOJ 4101 크냐?
import sys

for line in sys.stdin:
    a, b = map(int, line.split())
    if a == b == 0:
        break
    print("Yes" if a > b else "No")
