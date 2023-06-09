T = int(input())

for i in range(T):
    result = 0
    s = int(input())
    n = int(input())
    result += s
    if n != 0:
        for j in range(n):
            q, p = map(int, input().split())
            result += q * p
    print(result)

# T = 테스트 케이스의 개수
# s = 자동차의 가격 (1 <= s <= 100 000)
# n = 서로 다른 옵션의 개수(0 <= n <= 1000)
# q, p = 특정 옵션의 개수, 해당 옵션의 가격 (1 <= q <= 100, 1 <= p <= 10 000)