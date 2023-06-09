T = int(input())

for i in range(T):
    suup = int(input())
    total_C = 0
    total_G = 0
    for j in range(suup):
        C, G = map(float, input().split())
        total_C += C
        total_G += G * C

    print(int(total_C), "{:.1f}".format(total_G/total_C))

# T = 학기의 수, suup = 수강 과목의 수, C = 학점, G = 성적
