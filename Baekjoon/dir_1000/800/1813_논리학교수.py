import sys

cham = {}
cham_many = []
N = int(sys.stdin.readline())
blackboard = list(map(int, sys.stdin.readline().rstrip().split()))

for item in blackboard:
    if item in cham:
        cham[item] += 1
    else:
        cham[item] = 1

for cham_key in cham:
    if cham_key == cham.get(cham_key):
        cham_many.append(cham_key)


if cham_many:
    print(max(cham_many))
elif not cham_many and 0 in cham:
    print(-1)
else:
    print(0)

'''
N개의 말이 참이다 는 해당 문장이 N번 나오면 참이므로 딕셔너리를 이용해 N개가 몇번 나왔는지를 저장한 뒤
그 숫자들을 비교한 뒤 가장 큰 값을 출력하는 방식으로 구현 하였다.

그리고 모순에 대한 테스트케이스가 하나밖에 없어서 해당 부분을 적용하는게 조금은 어려웠는데
그 어떠한 문장도 참인 문장이 없는데 "0개의 말이 참이다" 라는 문장이 있는 경우가 모순되는 문장으로
이해하고 풀이하면 쉽게 풀이할 수 있다.
'''