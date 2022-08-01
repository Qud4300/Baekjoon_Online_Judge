# BOJ 11689 GCD(n,k) = 1
'''
  Euler's Phi function
임의의 양의 정수 m에 대해, m이하의 양의 정수 중 m과 서로소인 양의 정수의 개수를 구한다.
-> 정수 m의 '소인수 리스트'가 있다면, m과 서로소인 정수들을 쉽게 구할 수 있다.
-> m의 소인수 리스트 [p1,p2, ... , pn]와 이 소인수들의 지수 리스트 [k1,k2, ... , kn]가 있을 때, 아래의 식들이 성림.
-> Phi(m) = m * (1-1/p1) * (1-1/p2) * ... * (1-1/pn)이다.
-> 또한, 서로소인 양의 정수 m과 n에 대해 Phi(m) * Phi(n) == Phi(m*n)이 성립한다. (곱셈적 함수)
-> 어떤 소인수 p에 대해, Phi(p^k) = p^k - p^(k-1) = p^(k-1) * (p-1)이다.
-> 다시 말해, m = (p1^k1)(p2^k2)...(pn^kn)일 때, Phi(m) = Π(i:1~n){(pi-1) * i^(ki-1)}이고, 이 식을 문제해결에 사용한다..
.. 참고 : 오일러 정리.
'''
n = int(input())
factors = []
for i in range(2, int(n**0.5)+1):
    count = 0
    while n%i == 0:
        n //= i
        count += 1
    if count:
        factors.append([i, count])
    if n == 1:
        break
if n != 1:
    factors.append([n, 1])

phi = 1
for i, count in factors:
    phi *= (i-1)*i**(count-1)

print(phi)