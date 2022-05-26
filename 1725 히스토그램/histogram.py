# BOJ 1725 히스토그램
import sys
import math
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n = int(input())
nums = [0]+[int(input()) for _ in range(n)]
seg_tree = [None for _ in range((1 << math.ceil(math.log2(n + 1))+1) + 1)]


def make_tree(tree, start, end, v):
    if start == end:
        tree[v] = start
    else:
        mid = (start + end) // 2
        make_tree(tree, start, mid, v*2)
        make_tree(tree, mid+1, end, v*2+1)
        tree[v] = tree[v*2] if nums[tree[v*2]] <= nums[tree[v*2+1]] else tree[v*2+1]


def find_min(tree, start, end, v, left, right):
    if end < left or right < start:
        return None
    if left <= start and end <= right:
        return tree[v]
    else:
        mid = (start+end)//2
        m1 = find_min(tree, start, mid, v * 2, left, right)
        m2 = find_min(tree, mid + 1, end, v * 2 + 1, left, right)
        return m2 if m1 is None else m1 if m2 is None else m2 if nums[m2] < nums[m1] else m1


def find_rect(tree, start, end):
    m = find_min(tree, 1, n, 1, start, end)
    rect = nums[m]*(end-start+1)
    if start < m:
        rect = max(rect, find_rect(tree, start, m-1))
    if m < end:
        rect = max(rect, find_rect(tree, m+1, end))
    return rect


make_tree(seg_tree, 1, n, 1)
print(find_rect(seg_tree, 1, n))
