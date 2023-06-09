import sys

N, M = map(int, sys.stdin.readline().rstrip().split())
A, B = [], []
arr_result = [[] for _ in range(N)]

for _ in range(N):
    A.append(list(map(int, sys.stdin.readline().rstrip().split())))

for _ in range(N):
    B.append(list(map(int, sys.stdin.readline().rstrip().split())))

for i in range(N):
    for j in range(M):
        arr_result[i].append(str(A[i][j] + B[i][j]))

for i in range(len(arr_result)):
    print(" ".join(arr_result[i]))
