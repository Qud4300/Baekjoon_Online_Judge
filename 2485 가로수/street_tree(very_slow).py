# BOJ 2485 가로수

def gcd(a, b):
    if b>a:
        a,b = b,a
    while b != 0:
        a = a%b
        a,b = b,a
    return a


n = int(input())
arr = [int(input()) for _ in range(n)]
gap = [*map(lambda a, b: abs(a-b), arr[:-1], arr[1:])]
gap_sum = sum(gap)
gap_gcd = min(gap)
while len(gap):
    gap_gcd = gcd(gap_gcd, gap.pop())
    if gap_gcd == 1:
        break
print(gap_sum//gap_gcd-n+1)

