import sys

N = int(sys.stdin.readline().rstrip())
cnt = 0

for i in range(1, N + 1):
    result = 0
    for num in str(i):
        result += int(num)
    if i % result == 0:
        cnt += 1
print(cnt)
