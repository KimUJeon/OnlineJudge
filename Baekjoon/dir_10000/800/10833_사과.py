N = int(input())
remain_apple = 0

for i in range(N):
    student, apple = map(int, input().split())
    remain_apple += apple%student

print(remain_apple)

# N = 학교의 수를 나타내는 정수(1 <= N <= 100)