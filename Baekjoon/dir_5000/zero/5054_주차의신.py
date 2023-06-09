t = int(input())

for _ in range(t):
    n = int(input())
    xi = list(map(int, input().split()))

    parklot = sum(xi)//len(xi)
    length = (parklot - min(xi)) * 2 + (max(xi) - parklot) * 2

    print(length)