N = int(input())

if N == 1:
    print("*")

else:
    for i in range(N, 0, -1):
        if i == 1:
            print("*" + " *" * (N-1))
        else:
            print(" " * (i - 2) + " *" * (N - i + 1))