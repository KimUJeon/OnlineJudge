import sys

N, K = map(int, sys.stdin.readline().rstrip().split())
scores = list(map(int, sys.stdin.readline().rstrip().split()))
ratios = [4, 11, 23, 40, 60, 77, 89, 96, 100]
grade = list()

for score in scores:
    share = score*100//N
    for ratio in ratios:
        if share <= ratio:
            grade.append(str(ratios.index(ratio)+1))
            break

print(" ".join(grade))
