import sys

n = int(sys.stdin.readline().rstrip())

list_n: list = []
list_n += [int(sys.stdin.readline().rstrip()) for i in range(n)]
list_n.sort()

for item in list_n:
    print(item)

'''
input에 비해 sys.stdin.readline은 속도가 빠르기 때문에
이번 문제와 같이 N의 값이 기하급수적으로 크고 반복문이 많은 경우엔
sys.stdin.readline 을 사용해야 한다. 

input은 사용자가 입력하는 값을 모두 버퍼에 저장하는 특징이 있지만 readline은
한 줄 자체를 버퍼로 입력받는다. 그래서 readline은 개행문자 "\n" 도 입력받기 때문에
개행문자도 포함되는 불상사를 피하기 위해 rstrip() 을 사용한다.
'''
