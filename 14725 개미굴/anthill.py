# BOJ 14725 개미굴

class Node:
    def __init__(self, key: int):
        self.key = key
        self.children = {}

    def __str__(self):
        res = ''
        if self.key:
            res += str(self.key)
        if self.children:
            for key, val in sorted(list(self.children.items())):
                res += '\n--'+str(val).replace('\n', '\n--')
        return res


class Trie:
    def __init__(self):
        self.head = Node(None)

    def insert(self, strings:list):
        cur = self.head
        for c in strings:
            if c not in cur.children:
                cur.children[c] = Node(c)
            cur = cur.children[c]

    def __str__(self):
        res = ''
        for key, val in sorted(list(self.head.children.items())):
            res += '\n'+str(val)
        return res.strip()


n = int(input())
trie = Trie()
for _ in range(n):
    arr = input().split()[1:]
    trie.insert(arr)

print(str(trie))
