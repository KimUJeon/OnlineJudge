import sys

minkook = list(map(int, sys.stdin.readline().rstrip().split()))
manse = list(map(int, sys.stdin.readline().rstrip().split()))

sum_k = sum(minkook)
sum_s = sum(manse)

print(max(sum_s, sum_k))