import sys

words = sys.stdin.readline().rstrip()
count = 0

for idx in range(len(words)-3):
    if words[idx:idx+4] == "DKSH":
        count += 1

print(count)