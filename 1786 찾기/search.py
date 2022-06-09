# BOJ 1786 찾기

def LPS(pattern):
    # 패턴 : ex) aabaa 에서 LPS(Longest proper Prefix which is Suffix)는 aa.
    # ______ex) abaaba 에서 LPS는 aba.
    # ______ex) aabaaba 에서 LPS는 aaba.
    # 길이가 i+1인 문자열에서 길이가 v+1인 LPS가 있는지 탐색. i=1부터 시작.
    temp = [0 for _ in range(len(pattern))]
    v=0
    i=1
    while i < len(pattern):
        if pattern[i] == pattern[v]:
            v += 1
            temp[i] = v
            i += 1
            # 길이가 i+1인 부분문자열에서 길이가 v+1인 LPS가 존재한다.
        else:
            # LPS가 아니라면,
            if v != 0:
                # 이전 단계에서 발견한 LPS의 끝위치로 이동.
                v = temp[v-1]
            else:
                # i==0이면, 현재 길이 i의 LPS는 없음을 기록하고 탐색범위를 늘린다.
                temp[i] = 0
                i += 1
    return temp


def KMP(txt, pattern, lps):
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

text = input()
pat = input()
count, pos = KMP(text, pat, LPS(pat))
print(count)
print(*pos)
