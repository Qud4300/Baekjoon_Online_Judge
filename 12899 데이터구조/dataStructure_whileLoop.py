# BOJ 12899 데이터 구조
import sys
import math

input = sys.stdin.readline

size = 2000000
n = int(input())
seg_tree = [0 for _ in range((1 << int(math.ceil(math.log2(size + 1)))+1) + 1)]


def insert(tree, start, end, v, x):
    while start!=end:
        tree[v] += 1
        mid = (start + end) // 2
        if x <= mid:
            end = mid
            v = v*2
        else:
            start = mid+1
            v = v*2+1
    tree[v] += 1
    return


def pop(tree, start, end, v, x):
    while start != end:
        if tree[v] < 1:
            raise RuntimeError
        tree[v] -= 1
        mid = (start + end) // 2
        if x <= tree[v*2]:
            end = mid
            v = v * 2
        else:
            start = mid + 1
            x -= tree[v * 2]
            v = v * 2 + 1
    tree[v] -= 1
    return start


for T, X in [[*map(int, input().split())] for _ in range(n)]:
    if T == 1:
        insert(seg_tree, 1, size, 1, X)
    else:
        print(pop(seg_tree, 1, size, 1, X))
