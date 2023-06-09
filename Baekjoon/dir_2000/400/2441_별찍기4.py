N = int(input())

for i in range(N, 0, -1):
    if(i == N):
        print("*" * i)
    else:
        print(" " * (N - i) + "*" * i)