import sys

N = int(sys.stdin.readline().rstrip())
ans = 0
count = 0

while True:
    if '666' in str(ans):
        count += 1
    if count == N:
        print(ans)
        break
    ans += 1

'''
단순무식하지만 어렵게 생각하기 딱 좋은 문제
'''