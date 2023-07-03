import sys

N = int(sys.stdin.readline())
ans = 0

for i in range(1, N):
    temp_num = 0
    temp_num += i
    i = str(i)
    for item in i:
        temp_num += int(item)

    if temp_num == N:
        ans = i
        break

print(ans)