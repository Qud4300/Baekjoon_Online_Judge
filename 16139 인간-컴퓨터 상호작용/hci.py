#BOJ 16139 인간-컴퓨터 상호작용
import sys
input = sys.stdin.readline

string  = input().rstrip()
q = int(input())
query = [input().split() for _ in range(q)]
cumul = [[0 for _ in range(26)] for _ in range(len(string)+1)]
for i in range(len(string)):
    for alpha in range(26):
        cumul[i+1][alpha] = cumul[i][alpha]
    j = ord(string[i])-97
    cumul[i+1][j] = cumul[i][j] + 1

for a,l,r in query:
    o = ord(a)-97
    print(cumul[int(r)+1][o] - cumul[int(l)][o])

