N = int(input())

result = 0
for i in range(N+1):
    for j in range(i, N+1):
        result += i + j

print(result)

# N = 도미노 세트의 크기(1 <= N <= 1000)