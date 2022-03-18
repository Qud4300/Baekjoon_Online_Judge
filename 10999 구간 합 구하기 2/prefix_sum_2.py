# BOJ 10999 구간 합 구하기 2
import sys
import math
input = sys.stdin.readline

n, m, k = map(int, input().split())
nums = [0] + [int(input()) for _ in range(n)]
arr = [[*map(int, input().split())] for _ in range(m + k)]
nums_idx = [0 for _ in range(len(nums))]
seg_tree = [0 for _ in range((math.ceil(math.sqrt(n + 1))) ** 2 * 4 + 1)]
lazy_val = [0 for _ in range(len(seg_tree))]


def make_tree(tree, start, end, v):
    if start == end:
        tree[v] = nums[start]
    else:
        mid = (start + end) // 2
        tree[v] = make_tree(tree, start, mid, v * 2) + make_tree(tree, mid + 1, end, v * 2 + 1)
    return tree[v]


def sum_tree(tree, start, end, v, left, right):
    if lazy_val[v]:
        lazy_update(tree, start, end, v)
    if end < left or right < start:
        return 0
    elif left <= start and end <= right:
        return tree[v]
    else:
        mid = (start + end) // 2
        return sum_tree(tree, start, mid, v * 2, left, right) + sum_tree(tree, mid + 1, end, v * 2 + 1, left, right)


def lazy_update(tree, start, end, v):
    tree[v] += (end - start + 1) * lazy_val[v]
    if start != end:
        lazy_val[v * 2] += lazy_val[v]
        lazy_val[v * 2 + 1] += lazy_val[v]
    lazy_val[v] = 0
    return


def update_tree(tree, start, end, v, left, right, dif):
    if lazy_val[v]:
        lazy_update(tree, start, end, v)
    if end < left or right < start:
        return
    elif left <= start and end <= right:
        tree[v] += (end - start + 1) * dif
        if start != end:
            lazy_val[v * 2] += dif
            lazy_val[v * 2 + 1] += dif
        return
    else:
        mid = (start + end) // 2
        update_tree(tree, start, mid, v * 2, left, right, dif)
        update_tree(tree, mid + 1, end, v * 2 + 1, left, right, dif)
        tree[v] = tree[v*2] + tree[v*2+1]
        return


make_tree(seg_tree, 1, n, 1)
res = ''

for a in arr:
    if a[0] == 1:
        update_tree(seg_tree, 1, n, 1, a[1], a[2], a[3])
    elif a[0] == 2:
        res += str(sum_tree(seg_tree, 1, n, 1, a[1], a[2])) + '\n'

print(res.rstrip())
