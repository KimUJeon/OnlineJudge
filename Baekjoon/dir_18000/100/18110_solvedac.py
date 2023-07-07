import sys
from collections import deque

n = int(sys.stdin.readline().rstrip())
ans = []
cut = round(n*0.15 + 0.00001)

if n == 0:
    print(0)

else:
    for _ in range(n):
        ans.append(int(sys.stdin.readline().rstrip()))
    ans.sort()
    ans = deque(ans)

    for i in range(cut):
        ans.popleft()
        ans.pop()

    fin_ans = round(sum(ans)/(n-(2 * cut)) + 0.00001)
    print(fin_ans)