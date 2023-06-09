'''
import sys
from itertools import permutations

N, M = map(int, sys.stdin.readline().rstrip().split())
lst = [i for i in range(1, N+1)]
arr = [list(row) for row in permutations(lst, M)]

for item in arr:
    print(*item)


Python 리스트의 Asterisk(*) 을 사용하면 리스트 압축 해제를 할 수 있어 위와같이 풀이가 가능함
'''
import sys
def dfs():
    if len(s) == m:
        print(' '.join(map(str, s)))
        return
    for i in range(1, n + 1):
        if i in s:
            continue
        s.append(i)
        dfs()
        s.pop()


n, m = map(int, sys.stdin.readline().rstrip().split())
s = []

dfs()