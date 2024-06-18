import sys

N = int(sys.stdin.readline())

group = [N]
l_group = [N]
for i in range(N, 0, -1):
    group.append(i)
    while True:
        value = group[-2] - group[-1]
        if value >= 0:
            group.append(value)
        else:
            break

    if len(group) >= len(l_group):
        l_group = group
    group = [N]

print(len(l_group))
for item in l_group:
    print(item, end=" ")
