import sys

digits = 9 * 1 + 7 * 3 + 8 * 1 + 0 * 3 + 9 * 1 + 2 * 3 + 1 * 1 + 4 * 3 + 1 * 1 + 8 * 3
for i in range(3):
    if i % 2 == 0:
        digits += int(sys.stdin.readline().rstrip()) * 1
    else:
        digits += int(sys.stdin.readline().rstrip()) * 3

print(f"The 1-3-sum is {digits}")