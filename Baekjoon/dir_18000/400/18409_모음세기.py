import sys

N = int(sys.stdin.readline())
S = sys.stdin.readline().rstrip()
count = 0

for word in S:
    if word == 'a' or word == 'e' or word == 'i' or word =='o' or word =='u':
        count += 1

print(count)