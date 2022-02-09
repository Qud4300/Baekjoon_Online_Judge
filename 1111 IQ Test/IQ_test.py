# BOJ 1111 IQ Test

n = int(input())
arr = [*map(int, input().split())]

if n < 3:
    if n == 1:
        print('A')
    elif arr[0]==arr[1]:
        print(arr[0])
    else:
        print('A')
else:
    x,y,z = arr[:3]
    if x==y:
        if x==y==z:
            for i in arr[3:]:
                if i != z:
                    print('B')
                    exit()
            print(x)
        else:
            print('B')
    else:
        a = (z-y)/(y-x)
        if int(a) != a:
            print('B')
        else:
            a = int(a)
            b = y-a*x
            for i in range(3, n):
                if arr[i] != arr[i-1] * a+b:
                    print('B')
                    exit()
            print(arr[-1]*a+b)
