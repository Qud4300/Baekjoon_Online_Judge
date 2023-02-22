# BOJ 1269 대칭차집합

input()
a = set([*map(int, input().split())])
b = set([*map(int, input().split())])
print(len(a.symmetric_difference(b)))