total = []

for i in range(4):
    goout, goin = map(int, input().split())
    now = goin - goout
    if i == 0:
        total.append(now)
    else:
        total.append(total[i-1] + now)
print(max(total))