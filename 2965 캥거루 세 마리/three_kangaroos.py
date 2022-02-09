# BOJ 2965 캥거루 세 마리

a, b, c = map(int, input().split())
count = 0
while not a == b-1 == c-2:
    if abs(a-b) > abs(b-c):
        c = b-1
    else:
        a = b+1
    a,b,c = sorted([a,b,c])
    count += 1
print(count) 
