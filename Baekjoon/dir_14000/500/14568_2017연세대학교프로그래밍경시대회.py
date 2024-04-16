import sys

N = int(sys.stdin.readline().rstrip())
cnt = 0

for i in range(2, N - 1, 2):
    # 택희는 항상 2개씩 가져가야 하고 남규가 영훈이보다 2개를 더 가져가야 하기 때문에 -i -2 를 한것
    cnt += (N - i - 2) // 2

print(cnt)
