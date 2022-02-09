# BOJ 1072 게임
import sys

percent = lambda a, b: int((b*100 / a))

for line in sys.stdin:
    x, y = map(int, line.split())
    z = percent(x, y)
    l, r = 1, 1000000000
    while l < r:
        m = (l+r)//2
        if percent(x+m, y+m) <= z:
            l = m+1
        else:
            r = m
    print(r if percent(x+r, y+r) > z else -1)
