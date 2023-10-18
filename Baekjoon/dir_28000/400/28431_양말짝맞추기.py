import sys

socks = list()
for _ in range(5):
    socks.append(sys.stdin.readline().rstrip())

for item in socks:
    flag = False
    target_sock = item
    cnt = socks.count(target_sock)
    while flag == False:
        if cnt >= 2:
            socks.remove(target_sock)
            socks.remove(target_sock)
            cnt -= 2
        else:
            flag = True
print(socks[0])