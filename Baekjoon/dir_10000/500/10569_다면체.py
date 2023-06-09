T = int(input())

for i in range(T):
    V, E = map(int, input().split())
    print(E-V+2)

# T = 테스트 케이스의 수
# V = 꼭짓점의 수, E = 모서리의 수
# 임의의 볼록다면체는 (꼭짓점의 수) - (모서리의 수) + (면의 수) = 2 가 성립한다