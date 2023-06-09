K = int(input())

for _ in range(K):
    want = []
    P, M = map(int, input().split())
    for i in range(P):
        want.append(int(input()))
    want = list(set(want))
    print(P - len(want))