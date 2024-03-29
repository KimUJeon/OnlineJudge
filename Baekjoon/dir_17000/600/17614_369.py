import sys

N = int(sys.stdin.readline().rstrip())
count = 0

for i in range(1, N + 1):
    for word in str(i):
        if word == "3" or word == "6" or word == "9":
            count += 1

print(count)
