# BOJ 1406 에디터
import sys
input = sys.stdin.readline

buf1 = list(input().rstrip())
buf2 = []

for _ in range(int(input())):
    com = input()
    if com[0]=='L' and buf1:
        buf2.append(buf1.pop())
    elif com[0]=='D' and buf2:
        buf1.append(buf2.pop())
    elif com[0]=='B' and buf1:
        buf1.pop()
    elif com[0]=='P':
        buf1.append(com[2])

print(''.join(buf1)+''.join(reversed(buf2)))
