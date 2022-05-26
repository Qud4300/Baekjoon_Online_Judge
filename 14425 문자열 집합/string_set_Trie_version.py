# BOJ 14425 문자열 집합 using Trie
# Gets AC when submitted with PyPy3, not Python3
import sys

input = sys.stdin.readline


class Node:
    def __init__(self, key, data=None):
        self.key = key
        self.content = data
        self.children = {}


class Trie:
    def __init__(self):
        self.head = Node(None)

    def insert(self, t: str):
        cur = self.head
        for c in t:
            if c not in cur.children:
                cur.children[c] = Node(c)
            cur = cur.children[c]
        cur.content = t
        return

    def find(self, t: str):
        cur = self.head
        for c in t:
            if c in cur.children:
                cur = cur.children[c]
            else:
                return False
        if cur.content == t:
            return True
        return False


n, m = map(int, input().split())
S = Trie()
for _ in range(n):
    S.insert(input().rstrip())
count = 0
for _ in range(m):
    if S.find(input().rstrip()):
        count += 1
print(count)
