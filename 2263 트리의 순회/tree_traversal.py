# BOJ 2263 Tree Traversal
import sys
input = sys.stdin.readline

N = int(input())
inorder = input().split()
postorder = input().split()


def preorder(n, mid, post):
    res = []
    queue = [[0, n-1, 0, n-1]]
    loc = {mid[i]: i for i in range(n)}
    while queue:
        # l r for inorder, s e for postorder index
        l, r, s, e = queue.pop()
        root = post[e]
        root_loc = loc[root]
        res.append(root)
        l_size = root_loc-l
        if 0 <= root_loc < r:
            queue.append([root_loc+1, r, s+l_size, e-1])
        if 0 <= l < root_loc:
            queue.append([l, root_loc-1, s, s+l_size-1])
    return res


print(' '.join(preorder(N, inorder, postorder)))
