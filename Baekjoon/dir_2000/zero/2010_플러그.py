import sys

N = int(input())
result = 0

for i in range(1, N+1):
    result += int(sys.stdin.readline())

print(result - (N-1))

# N = 멀티탭의 개수 (1 <= N <= 500,000)
# 이번 문제는 알고리즘은 쉬우나 시간 제한을 고려해야 하기 때문에
# 입력을 빠르게 받아들일 수 있는 sys 를 활용하여 문제풀이를 해야 한다