# BOJ 1041 주사위
n = int(input())
a,b,c,d,e,f = map(int, input().split())

if n==1:
    print(sum([a,b,c,d,e,f]) - max(a,b,c,d,e,f))
else:
    min_3 = min(a+b+c, a+b+d, a+c+e, a+d+e, b+c+f, b+d+f, c+e+f, d+e+f)
    min_2 = min(a+b,a+c,a+d,a+e,b+c,b+d,b+f,c+e,c+f,d+e,d+f,e+f)
    if n==2:
        print(4*min_3+4*min_2)
    else:
        plane = 5*max(0, n-2)**2 + max(0,n-2)*4
        line_2 = max(0, n-2)*8+4
        point_3 = 4
        print(plane*min(a,b,c,d,e,f) + line_2*min_2 + point_3*min_3)
