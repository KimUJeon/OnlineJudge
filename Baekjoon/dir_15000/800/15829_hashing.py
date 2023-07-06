import sys

r = 31
M = 1234567891
L = int(sys.stdin.readline().rstrip())
words = sys.stdin.readline().rstrip()
ans = 0

for i in range(L):
    cur_idx = ord(words[i]) - 96
    ans += cur_idx * 31 ** i

print(ans % M)

