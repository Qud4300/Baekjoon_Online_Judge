# BOJ 12899 데이터 구조
import sys
import math

input = sys.stdin.readline

size = 2000000
n = int(input())
seg_tree = [0 for _ in range((1 << int(math.ceil(math.log2(size + 1)))+1) + 1)]


def insert(tree, start, end, v, x):
    tree[v] += 1
    if start==end:
        return
    mid = (start + end) // 2
    if x <= mid:
        insert(tree, start, mid, v*2, x)
    else:
        insert(tree, mid+1, end, v*2+1, x)
    return


def pop(tree, start, end, v, x):
    if tree[v]<1:
        raise RuntimeError
    tree[v] -= 1
    if start == end:
        return start
    mid = (start + end) // 2
    if x <= tree[v*2]:
        return pop(tree, start, mid, v * 2, x)
    else:
        return pop(tree, mid + 1, end, v * 2 + 1, x-tree[v*2])


for T, X in [[*map(int, input().split())] for _ in range(n)]:
    if T == 1:
        insert(seg_tree, 1, size, 1, X)
    else:
        print(pop(seg_tree, 1, size, 1, X))
