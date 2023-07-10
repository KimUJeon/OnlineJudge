import sys

row, col, inv = map(int, sys.stdin.readline().rstrip().split())
min_time = 1e9
ans_h = 0
blocks = []
for _ in range(row):
    blocks.append(list(map(int, sys.stdin.readline().rstrip().split())))

min_h = min(min(blocks))
max_h = max(max(blocks))

for i in range(min_h, max_h+1):
    over = 0
    under = 0

    for j in range(row):
        for k in range(col):
            if blocks[j][k] < i:
                under += i - blocks[j][k] # under 만큼 채워야 함
            elif blocks[j][k] > i:
                over += blocks[j][k] - i # over 만큼 깎아내리기

    # 기존 inv(인벤토리)를 사용하면 초기화가 되지 않는 문제가 있어 새로운 변수 사용
    inven = inv + over

    if inven < under:
        continue

    time = 2 * over + under

    if time <= min_time:
        min_time = time
        ans_h = i

print(min_time, ans_h)