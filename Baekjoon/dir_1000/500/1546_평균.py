test = []
total = 0
count = int(input())

test = list(map(int, input().split()))

max_value = max(test)

for i in range(count):
    score = test[i]/max_value*100
    total += score

avg = total/count
print(avg)


<문제>
세준이는 기말고사를 망쳤다. 세준이는 점수를 조작해서 집에 가져가기로 했다. 일단 세준이는 자기 점수 중에 최댓값을 골랐다. 
이 값을 M이라고 한다. 그리고 나서 모든 점수를 점수/M*100으로 고쳤다.
예를 들어, 세준이의 최고점이 70이고, 수학점수가 50이었으면 수학점수는 50/70*100이 되어 71.43점이 된다.
세준이의 성적을 위의 방법대로 새로 계산했을 때, 새로운 평균을 구하는 프로그램을 작성하시오.

<입력>
첫째 줄에 시험 본 과목의 개수 N이 주어진다. 이 값은 1000보다 작거나 같다.
둘째 줄에 세준이의 현재 성적이 주어진다. 이 값은 100보다 작거나 같은 음이 아닌 정수이고, 적어도 하나의 값은 0보다 크다.
ex.1) 3
40 80 60

ex.2) 3
10 20 30

ex.3) 5
1 2 4 8 16

<출력>
첫째 줄에 새로운 평균을 출력한다. 실제 정답과 출력값의 절대오차 또는 상대오차가 10-2 이하이면 정답이다.
ex.1) 75.0

ex.2) 66.666667
# 10-2 이하의 오차를 허용한다는 말은 정확히 소수 2번째 자리까지 출력하라는 뜻이 아니다.

ex.3) 38.75

<해설>
list(map(int, input().split()))을 이용해 리스트를 만들고
max 함수를 이용해 가장 큰 값을 구한뒤 문제에 주어진 대로 계산식에 대입한 후
실행시키면 된다.
