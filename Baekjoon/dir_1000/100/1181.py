import sys

N = int(sys.stdin.readline())
all_word = []

for _ in range(N):
	all_word.append(sys.stdin.readline().rstrip())

all_word = list(set(all_word))
all_word.sort()
all_word.sort(key=len)

print("\n".join(all_word))