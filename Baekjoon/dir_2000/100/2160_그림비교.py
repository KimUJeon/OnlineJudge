import sys

# sys.stdin = open("input.txt", "rt") # 절대 경로, 상대 경로 가능

N = int(sys.stdin.readline())
paint = [[] for _ in range(N)]
min_p1 = min_p2 = 0
min_diff = 36
cnt = 0

while cnt < N:
    for _ in range(5):
        paint[cnt].append(sys.stdin.readline().rstrip())
    cnt += 1
for p1 in range(N):
    for p2 in range(p1 + 1, N):
        tmp = 0
        for row in range(5):
            for col in range(7):
                if paint[p1][row][col] != paint[p2][row][col]:
                    tmp += 1
        if tmp < min_diff:
            min_diff = tmp
            min_p1, min_p2 = p1, p2
print(min_p1 + 1, min_p2 + 1)

'''
브루트포스 알고리즘 문제, 문제를 간단히 설명하자면
열 = 5, 행 = 7 로 이루어진 직사각형의 그림이 N개가 주어진다는 의미
그림을 p1, p2로 뽑아 내부를 비교한 뒤 카운트된 tmp가 작다면 min_diff 값을 tmp로 바꿔주는 식으로 구현

예제 입력 하나하나 입력하기 싫어서 파일 입력방식으로 했지만 제출할땐 주석처리 해야 함
'''