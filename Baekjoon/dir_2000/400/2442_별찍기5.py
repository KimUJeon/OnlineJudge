N = int(input())
j = 1

for i in range(N, 0, -1):
    print(" " * (i-1) + "*" * (2*j-1))
    j += 1