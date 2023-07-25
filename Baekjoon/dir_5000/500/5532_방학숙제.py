import sys

L = int(sys.stdin.readline().rstrip())
A = int(sys.stdin.readline().rstrip())
B = int(sys.stdin.readline().rstrip())
C = int(sys.stdin.readline().rstrip())
D = int(sys.stdin.readline().rstrip())
lang, mat = 0, 0

if A % C == 0:
    lang += A//C
else:
    lang += A//C + 1

if B % D == 0:
    mat += B//D
else:
    mat += B//D + 1

print(L - max(lang, mat))