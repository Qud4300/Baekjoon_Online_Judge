# BOJ 5670 휴대폰 자판
import sys
input = sys.stdin.readline


class Node:
    def __init__(self, key: str, content: str = None):
        self.key = key
        self.children = {}
        self.content = content


class Trie:
    def __init__(self):
        self.head = Node(None)

    def insert(self, text: str = None):
        if text is None:
            return
        cur = self.head
        for c in text:
            if c not in cur.children:
                cur.children[c] = Node(c)
            cur = cur.children[c]
        cur.content = text
        return

    def stat(self):
        stage = []
        for node in self.head.children.values():
            stage.append((node, 1))
        res = []
        while stage:
            next_stage = []
            while stage:
                node, count = stage.pop()
                if node.content:
                    res.append(count)
                flag = 1 if len(node.children)>1 or (node.content and node.children) else 0
                for child in node.children.values():
                    next_stage.append((child, count + flag))
            stage = next_stage
        return sum(res)/len(res)


while True:
    try:
        n = int(input())
        trie = Trie()
        for _ in range(n):
            trie.insert(input().rstrip())
        print(f'{trie.stat():.2f}')
    except:
        break
