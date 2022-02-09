# BOJ 1963 소수 경로
import sys
input = sys.stdin.readline


def sieve(a, b):
    arr = [i for i in range(b + 1)]
    arr[0], arr[1] = False, False
    for i in range(2, int(b ** 0.5 + 1)):
        if arr[i] != 0:
            for j in range(i + i, b + 1, i):
                arr[j] = 0
    return arr[a:b + 1]


def diff(a, b):
    a, b = str(a), str(b)
    difference = 0
    for i in range(len(a)):
        if a[i] != b[i]:
            difference += 1
    return difference


count = 0
primes = []
where = dict()
for i in sieve(1000, 9999):
    if i != 0:
        primes.append(i)
        where[i] = count
        count += 1


def bfs(a, b):
    if a == b:
        return 0
    visited = set()
    stage = [a]
    stage_count = 0
    while stage:
        next_stage = []
        for cur in stage:
            for k in [1000, 100, 10, 1]:
                remain = (cur // (k * 10))*k*10 + cur % k
                for n in range(0, 10):
                    tar = remain + n * k
                    if tar not in visited and tar in where:
                        if tar == b:
                            return stage_count+1
                        next_stage.append(tar)
                        visited.add(tar)
        stage = next_stage
        stage_count += 1
    return -1


for TEST_CASE in range(int(input())):
    A, B = map(int, input().split())
    res = bfs(A, B)
    print(res if res != -1 else "Impossible")
