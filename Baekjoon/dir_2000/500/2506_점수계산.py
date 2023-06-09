N = int(input())
score = 0
sum_score = 0

problems = list(map(int, input().split()))

for i in range(N):
    if problems[i] == 1:
        score += 1
        sum_score += score
    else:
        score = 0

print(sum_score)