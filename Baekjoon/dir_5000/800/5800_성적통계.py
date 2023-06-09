K = int(input())

for _ in range(K):
    score = list(map(int, input().split()))
    people = score[0]

    gap = 0
    score.remove(people)

    for i in range(people-1):
        score.sort()
        if gap < score[i+1] - score[i]:
            gap = score[i+1] - score[i]


    print("Class %d"%(_+1))
    print("Max %d, Min %d, Largest gap %d"%(max(score), min(score), gap))