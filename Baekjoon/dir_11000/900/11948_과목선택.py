import sys

A = int(sys.stdin.readline().rstrip())
B = int(sys.stdin.readline().rstrip())
C = int(sys.stdin.readline().rstrip())
D = int(sys.stdin.readline().rstrip())
E = int(sys.stdin.readline().rstrip())
F = int(sys.stdin.readline().rstrip())

science = [A, B, C, D]
inmun = [E, F]

science.sort(reverse=True)
inmun.sort(reverse=True)
result = 0

for item in science[:3]:
    result += item
result += inmun[0]
print(result)