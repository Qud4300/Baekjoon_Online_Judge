# BOJ 2042 구간 합 구하기
import sys
import math

input = sys.stdin.readline

n, m, k = map(int, input().split())
nums = [0] + [int(input()) for _ in range(n)]
arr = [[*map(int, input().split())] for _ in range(m + k)]
seg_tree = [0 for _ in range((math.ceil(math.sqrt(n + 1))) ** 2 * 4 + 1)]


def make_tree(tree, start, end, v):
    if start == end:
        tree[v] = nums[start]
    else:
        mid = (start + end) // 2
        tree[v] = make_tree(tree, start, mid, v * 2) + make_tree(tree, mid + 1, end, v * 2 + 1)
    return tree[v]


def sum_tree(tree, start, end, v, left, right):
    if end < left or right < start:
        return 0
    elif left <= start and end <= right:
        return tree[v]
    else:
        mid = (start + end) // 2
        return sum_tree(tree, start, mid, v * 2, left, right) + sum_tree(tree, mid + 1, end, v * 2 + 1, left, right)


def update_tree(tree, start, end, v, idx, dif):
    if idx < start or idx > end:
        return
    tree[v] += dif
    if start == end:
        return
    mid = (start + end) // 2
    update_tree(tree, start, mid, v * 2, idx, dif)
    update_tree(tree, mid + 1, end, v * 2 + 1, idx, dif)
    return


make_tree(seg_tree, 1, n, 1)
res = ''

for a, b, c in arr:
    if a == 1:
        update_tree(seg_tree, 1, n, 1, b, c - nums[b])
        nums[b] = c
    elif a == 2:
        res += str(sum_tree(seg_tree, 1, n, 1, b, c)) + '\n'

print(res.rstrip())
