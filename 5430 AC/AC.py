#BOJ 5430 AC
import sys
from collections import deque
# input = sys.stdin.readline

for _ in range(int(input())):
    com = input()
    n = int(input())
    if n==0:
        input()
        deq = deque()
    else:
        deq = deque(list(map(int, list(input()[1:-1].split(',')))))
    flag = False
    error = False
    for c in com:
        if c=='R':
            flag = not flag
        elif c=='D':
            try:
                if flag:
                    deq.pop()
                else:
                    deq.popleft()
            except:
                error = True
                break
        else:
            error = True
            break
    if error:
        print("error")
    else:
        if flag:
            deq.reverse()
        print('['+','.join(map(str,deq))+']')
