# BOJ 1517 버블 소트
import sys
import math
input = sys.stdin.readline

n = int(input())
nums = [0] + [*map(int, input().split())]
M = max(nums)
seg_tree = [None for _ in range((math.ceil(math.sqrt(n + 1))) ** 2 * 4 + 1)]


def merge(a, b):
    temp = []
    count = 0
    a_size = len(a)
    i, j = 0, 0
    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            temp.append(a[i])
            i += 1
            if a_size > 0:
                a_size -= 1
        else:
            temp.append(b[j])
            j += 1
            count += a_size
    while i < len(a):
        temp.append(a[i])
        i += 1
    while j < len(b):
        temp.append(b[j])
        j += 1
    return count, temp


def make_tree(tree, start, end, v):
    if start == end:
        return 0, [nums[start]]
    else:
        mid = (start + end) // 2
        left = make_tree(tree, start, mid, v*2)
        right = make_tree(tree, mid+1, end, v*2+1)
        count, merged = merge(left[1], right[1])

        return left[0] + right[0] + count, merged


print(make_tree(seg_tree, 1, n, 1)[0])
