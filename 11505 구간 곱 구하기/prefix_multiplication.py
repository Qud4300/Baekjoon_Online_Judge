# BOJ 11505 구간 곱 구하기
import sys
import math

P = 1000000007
input = sys.stdin.readline

n, m, k = map(int, input().split())
nums = [0] + [int(input()) for _ in range(n)]
arr = [[*map(int, input().split())] for _ in range(m + k)]
seg_tree = [0 for _ in range((math.ceil(math.sqrt(n + 1))) ** 2 * 4 + 1)]


def make_tree(tree, start, end, v):
    if start == end:
        tree[v] = nums[start] % P
    else:
        mid = (start + end) // 2
        tree[v] = (make_tree(tree, start, mid, v * 2) * make_tree(tree, mid + 1, end, v * 2 + 1)) % P
    return tree[v]


def mul_tree(tree, start, end, v, left, right):
    if end < left or right < start:
        return 1
    elif left <= start and end <= right:
        return tree[v]
    else:
        mid = (start + end) // 2
        return (mul_tree(tree, start, mid, v * 2, left, right)
                * mul_tree(tree, mid + 1, end, v * 2 + 1, left, right)
                ) % P


def update_tree(tree, start, end, v, idx, old, new):
    if start <= idx <= end:
        if start != end:
            mid = (start + end) // 2
            tree[v] = (update_tree(tree, start, mid, v * 2, idx, old, new)
                       * update_tree(tree, mid + 1, end, v * 2 + 1, idx, old, new)
                       ) % P
        elif start == idx:
            tree[v] = new
    return tree[v]


make_tree(seg_tree, 1, n, 1)
res = ''

for a, b, c in arr:
    if a == 1:
        update_tree(seg_tree, 1, n, 1, b, nums[b], c)
        nums[b] = c
    elif a == 2:
        res += str(mul_tree(seg_tree, 1, n, 1, b, c)) + '\n'

print(res.rstrip())
