# BOJ 10158 개미

w, h = map(int, input().split())
p, q = map(int, input().split())
t = int(input())

p = w - (p+t)%w if ((p+t)//w)%2 else (p+t)%w
q = h - (q+t)%h if ((q+t)//h)%2 else (q+t)%h

print(p, q)
