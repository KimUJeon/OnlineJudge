T = int(input())

for _ in range(T):
    scores = list(map(int, input().split()))

    scores.remove(max(scores))
    scores.remove(min(scores))

    if max(scores) - min(scores) >= 4:
        print("KIN")
    else:
        print(sum(scores))