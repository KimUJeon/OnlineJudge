N = int(input())

for i in range(N):
    r, e, c = map(int, input().split())
    profit = e - c

    if profit > r:
        print("advertise")
    elif profit == r:
        print("does not matter")
    else:
        print("do not advertise")
