import sys

cycle = int(sys.stdin.readline().rstrip())
print("Gnomes:")
for _ in range(cycle):
    orders = list(map(int, sys.stdin.readline().rstrip().split()))
    low_orders = sorted(orders)
    high_orders = list(reversed(low_orders))

    if orders == low_orders or orders == high_orders:
        print("Ordered")
    else:
        print("Unordered")