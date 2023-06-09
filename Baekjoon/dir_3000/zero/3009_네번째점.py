x_list = []
y_list = []

for i in range(3):
    x, y = map(int, input().split())
    x_list.append(x)
    y_list.append(y)

for i in range(3):
    if x_list.count(x_list[i]) == 1:
        x = x_list[i]
    if y_list.count(y_list[i]) == 1:
        y = y_list[i]

print(x, y)

<문제>
세 점이 주어졌을 때, 축에 평행한 직사각형을 만들기 위해서 필요한 네 번째 점을 찾는 프로그램을 작성하시오.

<입력>
세 점의 좌표가 한 줄에 하나씩 주어진다. 좌표는 1보다 크거나 같고, 1000보다 작거나 같은 정수이다.

<출력>
직사각형의 네 번째 점의 좌표를 출력한다.

<예제 입력 1> 
30 20
10 10
10 20

<예제 출력 1>
30 10

<해설>
x 와 y 를 3번 입력 받은뒤 리스트에 저장 시킨다.
그 뒤, x_list 에 i번째 인덱스에 존재하는 수가 1개라면 해당 값이 좌표이므로 x값에 저장시키고
y도 똑같은 방법으로 좌표를 구해 출력하면 되는 문제이다.
