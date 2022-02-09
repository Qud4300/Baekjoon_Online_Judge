# BOJ 1059 종은 구간

def res(a, s, e):
    """
    possible case 1: s < a < e
                 --: [(s~a-1) : (a+1~e)] + case 2 + case 3
    possible case 2: a : (a+1~e) => K = e-a
    possible case 3: (s~a-1) : a => L = a-s
        ==> K*L + K + L == K(L+1) + L == (K+1)*(L+1)-1
    """
    k, l = e - a, a - s
    return (k + 1) * (l + 1) - 1


int(input())
S = sorted([*map(int, input().split())])
n = int(input())

if S[-1] <= n or n < 1 or n > 1000:
    print(0)
elif n < S[0]:
    print(res(n, 1, S[0]-1))
else:
    for i in range(len(S)):
        if n == S[i]:
            print(0)
            exit()
        if n < S[i]:
            idx = i
            break
    print(res(n, S[idx-1]+1, S[idx]-1))
