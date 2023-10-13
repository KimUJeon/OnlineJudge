import sys

N, X = map(int, sys.stdin.readline().rstrip().split())
A = list(map(int, sys.stdin.readline().rstrip().split()))

compact_A = [A[i]+A[i+1] for i in range(len(A)-1)]
min_idx = compact_A.index(min(compact_A))

result = A[min_idx] * X + A[min_idx+1] * X
print(result)