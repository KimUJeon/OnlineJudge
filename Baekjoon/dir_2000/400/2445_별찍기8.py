N = int(input())

for i in range(1, N+1):
    print("*" * i + " " * ((2*N)- (2*i)) + "*" * i)
    if i == N:
        for j in range(1, N+1):
            print("*" * (N-j) + " " * (j*2) + "*" * (N-j))