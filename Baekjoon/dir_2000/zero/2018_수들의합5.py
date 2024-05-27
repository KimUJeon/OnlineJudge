import sys

N = int(sys.stdin.readline().rstrip())
end, sum, cnt = 0, 0, 0

for start in range(0, N):
    while sum < N and end < N:
        sum += end + 1
        end += 1
    if sum == N:
        cnt += 1
    # sum(총 합)이 N 값을 넘긴 경우 start 포인트가 옮겨지기 때문에 start 값을 다시 빼주어야 함
    sum -= start + 1

print(cnt)
