personality = []
n = int(input())

for i in range(n):
    personality.append(input().split())

# 람다 키를 x로 정하고 year, month, day 순으로 오름차순 정렬을 시킴
personality.sort(key=lambda x:(int(x[3]), int(x[2]), int(x[1])))

# 나이가 가장 적은사람
print(personality[-1][0])
# 나이가 가장 많은 사람
print(personality[0][0])

# 출력문 코드가 위와같이 구성된 이유는 나이가 많은 사람이 연도 숫자가 작기때문에 오름차순 법칙에 의해
# 첫 순서로 배정이 되어있고 나이가 적은 사람은 연도 숫자가 크기 때문에 뒷 순서로 배정이 되어있기 때문이다.