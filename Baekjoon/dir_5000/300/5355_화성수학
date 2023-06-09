T = int(input())

for i in range(T):
    case = map(str, input().split())
    for j in case:
        if j == '@':
            result *= 3
        elif j == '%':
            result += 5
        elif j == '#':
            result -= 7
        else:
            result = float(j)
    print('{:.2f}'.format(result))

