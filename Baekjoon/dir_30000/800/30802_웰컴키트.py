import sys

N = int(sys.stdin.readline())
size = list(map(int, sys.stdin.readline().split()))
T, P = map(int, sys.stdin.readline().split())

shirts = 0
for i in range(len(size)):
    if size[i] % T == 0:
        shirts += int(size[i] / T)
    else:
        shirts += int(size[i] / T) + 1

print(shirts)

pens = [int(sum(size) / P), sum(size) % P]
print(*pens)
