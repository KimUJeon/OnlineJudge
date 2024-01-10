import sys

A1 = int(sys.stdin.readline().rstrip())
A2 = int(sys.stdin.readline().rstrip())
A3 = int(sys.stdin.readline().rstrip())

cost_a1 = A2 * 2 + A3 * 4
cost_a2 = A1 * 2 + A3 * 2
cost_a3 = A1 * 4 + A2 * 2

print(min(cost_a1, cost_a2, cost_a3))