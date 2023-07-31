# BOJ 10816 숫자 카드 2
from collections import defaultdict

deck = defaultdict(int)
input()
for i in [*map(int, input().split())]:
    deck[i] += 1
input()
print(' '.join([str(deck[q]) for q in [*map(int,input().split())]]))