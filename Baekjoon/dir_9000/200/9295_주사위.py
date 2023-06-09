T = int(input())

for i in range(T):
    result = 0
    a, b = map(int, input().split())
    result = a + b
    print("Case %d:" %(i+1), result)