# BOJ 4796 캠핑

count = 1
while True:
    L, P, V = map(int, input().split())
    if L == P == V == 0:
        break
    print(f"Case {count}:", V // P * L + min(V % P, L))
    count += 1
