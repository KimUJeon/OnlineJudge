import sys

total_apple = int(sys.stdin.readline())
more_apple = int(sys.stdin.readline())

claud = (total_apple + more_apple) // 2
natalia = (total_apple - more_apple) // 2

print(claud)
print(natalia)