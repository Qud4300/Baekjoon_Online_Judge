# BOJ 3003 King,Queen,Rook,Bishop,Knight,Pawn

arr = [1, 1, 2, 2, 2, 8]
i = 0
res = []
for a in [*map(int, input().split())]:
    res.append(arr[i] - a)
    i += 1
print(*res)
