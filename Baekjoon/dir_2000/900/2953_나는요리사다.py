scores = []

for i in range(5):
    score = map(int, input().split())
    scores.append(sum(score))

print(int(scores.index(max(scores)) + 1),max(scores))