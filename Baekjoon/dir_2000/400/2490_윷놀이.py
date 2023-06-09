for i in range(3):
    yut = list(map(int, input().split()))
    res = sum(yut)

    if res == 1:
        print("C")
    elif res == 2:
        print("B")
    elif res == 3:
        print("A")
    elif res == 4:
        print("E")
    else:
        print("D")