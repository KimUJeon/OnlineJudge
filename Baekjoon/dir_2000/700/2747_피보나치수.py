n = int(input())
a, b = 0, 1
for i in range(n):
    a, b = b, a+b
print(a)

# 다른 사람 풀이 참고
# 해당 문제는 작동 시간도 중요함