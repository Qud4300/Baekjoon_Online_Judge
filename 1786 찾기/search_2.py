# BOJ 1786 찾기

def LPS(pattern):
    pi = [0 for _ in range(len(pattern))]
    v=0
    _i=1
    while _i < len(pattern):
        if pattern[_i] == pattern[v]:
            v += 1
            pi[_i] = v
            _i += 1
        else:
            if v != 0:
                v = pi[v-1]
            else:
                pi[_i] = 0
                _i += 1
    return pi


def KMP(txt:str, pattern:str, lps:list):
    i = 0
    j = 0
    _count = 0
    res = []
    while i < len(txt):
        if txt[i] == pattern[j]:
            if j == len(pattern)-1:
                _count += 1
                res.append(i-len(pattern)+2)
                j = lps[j]
            else:
                j += 1
            i += 1
        else:
            if j != 0:
                j = lps[j-1]
            else:
                i += 1

    return _count, res

text = input().rstrip()
pat = input().rstrip()
count, pos = KMP(text, pat, LPS(pat))
print(count)
print(*pos)
