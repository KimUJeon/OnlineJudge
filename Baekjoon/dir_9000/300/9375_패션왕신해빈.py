import sys


n = int(sys.stdin.readline().rstrip())
combi = dict()
for _ in range(n):
    line = int(sys.stdin.readline().rstrip())
    combination = 1
    combi.clear()

    for j in range(line):
        detail, category = map(str, sys.stdin.readline().rstrip().split())
        if category in combi:
            combi[category] += 1
        else:
            # 해당 의상을 착용할지 안할지는 자유
            combi[category] = 2

    for value in combi.values():
        combination *= value

    # 의상을 모두 입지 않은 알몸의 경우를 제외
    print(combination - 1)
