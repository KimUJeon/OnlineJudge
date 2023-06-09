N = int(input())

for i in range(1, N+1):
    print(" " * (N-i) + "*" * (2*i-1))
    if i == N:
        for j in range(1, N):
            print(" " * j + "*" * (2*(N-j)-1))