import sys

formula = list(map(str, sys.stdin.readline().rstrip().split()))
oper_sum = int(formula[0]) + int(formula[2])

if oper_sum == int(formula[-1]):
    print("YES")
else:
    print("NO")