# BOJ 2357 최솟값과 최댓값
import sys
import math
input = sys.stdin.readline

n, m = map(int, input().split())
nums = [0]+[int(input()) for _ in range(n)]
pairs = [[*map(int, input().split())] for _ in range(m)]
seg_tree = [0 for _ in range((math.ceil(math.sqrt(n + 1))) ** 2 * 4 + 1)]


def make_tree(tree, start, end, v):
    if start == end:
        tree[v] = (nums[start], nums[start])
    else:
        mid = (start + end) // 2
        m1, M1 = make_tree(tree, start, mid, v * 2)
        m2, M2 = make_tree(tree, mid + 1, end, v * 2 + 1)
        tree[v] = (min(m1, m2), max(M1, M2))
    return tree[v]


def find_minMax(tree, start, end, v, left, right):
    if end < left or right < start:
        return sys.maxsize, -1
    elif left <= start and end <= right:
        return tree[v]
    else:
        mid = (start + end) // 2
        m1, M1 = find_minMax(tree, start, mid, v * 2, left, right)
        m2, M2 = find_minMax(tree, mid + 1, end, v * 2 + 1, left, right)
        return min(m1, m2), max(M1, M2)


make_tree(seg_tree, 1, n, 1)
res = ''

for a, b in pairs:
    m, M = find_minMax(seg_tree, 1, n, 1, a, b)
    res += str(m) + ' ' + str(M) + '\n'

print(res.rstrip())
