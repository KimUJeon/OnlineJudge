import sys

K, N = map(int, sys.stdin.readline().rstrip().split())
lines = []

for _ in range(K):
    lines.append(int(sys.stdin.readline().rstrip()))

start, end = 1, max(lines)

while start <= end:
    mid_val = (start + end) // 2
    count = 0

    for item in lines:
        count += item//mid_val
    if count>= N:
        # 랜선 개수가 원하는 것 보다 많은 경우 해당 랜선의 길이보다 더 긴 길이가 존재할 수 있기 때문에
        # 중간값보다 1을 키워 다시 돌려보고 만약 없는 경우라면 else로 들어가 새로운 중간값이 생성되어 이를 반복하면 
        # 원하는 값이 나옴
        start = mid_val + 1
    else:
        end = mid_val - 1

print(end)
