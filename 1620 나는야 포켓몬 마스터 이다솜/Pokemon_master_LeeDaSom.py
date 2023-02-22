# BOJ 1620 나는야 포켓몬 마스터 이다솜
import sys

lines = sys.stdin.readlines()
n =int(lines[0].split()[0])
dic = dict()
for i in range(1, n+1):
    name = lines[i].rstrip()
    dic[str(i)] = name
    dic[name] = str(i)
print('\n'.join(map(dic.get, map(str.rstrip, lines[n+1:]))))