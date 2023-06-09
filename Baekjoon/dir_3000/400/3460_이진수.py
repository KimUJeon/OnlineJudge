T = int(input())

for _ in range(T):
    n = bin(int(input()))[2:]
    for i in range(len(n)):
        if n[-i-1] == '1':
            print(i, end=' ')


# bin 은 10진수를 2진수로 변환해 주는 함수이며
# 2진수 값의 역순을 봐야 하기 때문에 [-i-1] 을 사용하였다.