T = int(input())

for _ in range(T):
    result = 0
    N, M = map(int, input().split())
    for i in range(N, M+1):
        i = str(i)
        result += i.count("0")
    print(result)