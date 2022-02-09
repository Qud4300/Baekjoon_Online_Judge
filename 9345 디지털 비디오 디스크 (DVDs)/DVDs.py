# BOJ 9345 디지털 비디오 디스크(DVDs)
import sys
import math
input = sys.stdin.readline


def make_tree(tree, start, end, v):
    if start == end:
        tree[v] = start, start
        return
    else:
        mid = (start + end) // 2
        make_tree(tree, start, mid, v * 2)
        make_tree(tree, mid + 1, end, v * 2 + 1)
        tree[v] = min(tree[v*2][0], tree[v*2+1][0]), max(tree[v*2][1], tree[v*2+1][1])
    return


def check_tree(tree, start, end, v, left, right):
    if end < left or right < start:
        return None
    elif left <= start and end <= right:
        return tree[v]
    else:
        mid = (start + end) // 2
        c1 = check_tree(tree, start, mid, v * 2, left, right)
        c2 = check_tree(tree, mid + 1, end, v * 2 + 1, left, right)
        if c1 and c2:
            return min(c1[0], c2[0]), max(c1[1], c2[1])
        elif c1:
            return c1
        elif c2:
            return c2


def update_tree(tree, start, end, v, idx, new):
    if idx < start or idx > end:
        return
    if start == end:
        tree[v] = (new, new)
        return
    mid = (start + end) // 2
    update_tree(tree, start, mid, v * 2, idx, new)
    update_tree(tree, mid + 1, end, v * 2 + 1, idx, new)
    tree[v] = min(tree[v*2][0], tree[v*2+1][0]), max(tree[v*2][1], tree[v*2+1][1])
    return


for TEST_CASE in range(int(input())):
    n, k = map(int, input().split())
    arr = [[*map(int, input().split())] for _ in range(k)]
    shelf = [i for i in range(n)]
    seg_tree = [0 for _ in range((math.ceil(math.sqrt(n + 1))) ** 2 * 4 + 1)]
    make_tree(seg_tree, 0, n-1, 1)
    res = ''
    for q, a, b in arr:
        if q == 0:
            update_tree(seg_tree, 0, n - 1, 1, a, shelf[b])
            update_tree(seg_tree, 0, n - 1, 1, b, shelf[a])
            shelf[a], shelf[b] = shelf[b], shelf[a]
        else:
            chk = check_tree(seg_tree, 0, n-1, 1, a, b)
            res += "YES\n" if (chk[0]==a and chk[1]==b) else "NO\n"
    print(res.rstrip())


----------------------------------------------------------------------------------

# BOJ 9345 디지털 비디오 디스크(DVDs)
import sys
import math
input = sys.stdin.readline


def make_tree(tree, start, end, v):
    if start == end:
        tree[v] = start, start
        return
    else:
        mid = (start + end) // 2
        make_tree(tree, start, mid, v * 2)
        make_tree(tree, mid + 1, end, v * 2 + 1)
        tree[v] = tree[v*2][0], tree[v*2+1][1]
    return


def check_tree(tree, start, end, v, left, right):
    if end < left or right < start:
        return True
    elif left <= start and end <= right:
        return left <= tree[v][0] and tree[v][1] <= right
    else:
        mid = (start + end) // 2
        return check_tree(tree, start, mid, v * 2, left, right) and check_tree(tree, mid + 1, end, v * 2 + 1, left, right)


def update_tree(tree, start, end, v, idx, new):
    if idx < start or idx > end:
        return
    if start == end:
        tree[v] = (new, new)
        return
    mid = (start + end) // 2
    update_tree(tree, start, mid, v * 2, idx, new)
    update_tree(tree, mid + 1, end, v * 2 + 1, idx, new)
    tree[v] = min(tree[v*2][0], tree[v*2+1][0]), max(tree[v*2][1], tree[v*2+1][1])
    return


for TEST_CASE in range(int(input())):
    n, k = map(int, input().split())
    arr = [[*map(int, input().split())] for _ in range(k)]
    shelf = [i for i in range(n)]
    seg_tree = [0 for _ in range((math.ceil(math.sqrt(n + 1))) ** 2 * 4 + 1)]
    make_tree(seg_tree, 0, n-1, 1)
    res = ''
    for q, a, b in arr:
        if q == 0:
            update_tree(seg_tree, 0, n - 1, 1, a, shelf[b])
            update_tree(seg_tree, 0, n - 1, 1, b, shelf[a])
            shelf[a], shelf[b] = shelf[b], shelf[a]
        else:
            chk = check_tree(seg_tree, 0, n-1, 1, a, b)
            res += "YES\n" if chk else "NO\n"
    print(res.rstrip())
