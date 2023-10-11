import sys

sent = sys.stdin.readline().rstrip()
MOBIS = ['M', 'O', 'B', 'I', 'S']
flag = True

for mobi in MOBIS:
    if mobi not in sent:
        flag = False
        break

if not flag:
    print("NO")
else:
    print("YES")
