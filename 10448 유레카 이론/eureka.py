# BOJ 10448 유레카 이론
import sys
input = sys.stdin.readline

arr = []
s = set()
i = 1
while i * (i + 1) // 2 < 1001:
    arr.append(i * (i + 1) // 2)
    i += 1

for i in range(len(arr)):
    for j in range(i, len(arr)):
        if arr[i] + arr[j] not in s:
            s.add(arr[i] + arr[j])

for TEST_CASE in range(int(input())):
    k = int(input())
    flag = False
    for a in arr:
        if a > k-2:
            break
        if k-a in s:
            flag = True
            break
    if not flag:
        print(0)
    else:
        print(1)