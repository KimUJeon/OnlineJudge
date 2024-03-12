import sys

N, M = map(int, sys.stdin.readline().rstrip().split())
man_dict = dict()
changed_list = list()
for _ in range(N):
    listen = sys.stdin.readline().rstrip()
    man_dict[listen] = 1

for _ in range(M):
    see = sys.stdin.readline().rstrip()
    try:
        man_dict[see] += 1
    except KeyError:
        pass

for man, cnt in man_dict.items():
    if cnt == 2:
        changed_list.append(man)

changed_list.sort()
print(len(changed_list))
for person in changed_list:
    print(person)
