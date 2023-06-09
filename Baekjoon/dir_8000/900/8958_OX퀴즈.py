test_case = int(input())

for i in range(test_case):
    case = list(map(str, input()))
    score = 0
    count = 0
    for j in range(len(case)):
        if case[j] == 'O':
            count += 1
            score += count
        elif case[j] == 'X':
            score += 0
            count = 0
    print(score)


<문제>
"OOXXOXXOOO"와 같은 OX퀴즈의 결과가 있다. O는 문제를 맞은 것이고, X는 문제를 틀린 것이다. 
문제를 맞은 경우 그 문제의 점수는 그 문제까지 연속된 O의 개수가 된다. 예를 들어, 10번 문제의 점수는 3이 된다.
"OOXXOXXOOO"의 점수는 1+2+0+0+1+0+0+1+2+3 = 10점이다.
OX퀴즈의 결과가 주어졌을 때, 점수를 구하는 프로그램을 작성하시오.

<입력>
첫째 줄에 테스트 케이스의 개수가 주어진다.
각 테스트 케이스는 한 줄로 이루어져 있고, 길이가 0보다 크고 80보다 작은 문자열이 주어진다. 문자열은 O와 X만으로 이루어져 있다.

5
OOXXOXXOOO
OOXXOOXXOO
OXOXOXOXOXOXOX
OOOOOOOOOO
OOOOXOOOOXOOOOX

<출력>
각 테스트 케이스마다 점수를 출력한다.

10
9
7
55
30

<해설>
case 가 개별적인 테스트 케이스이며 이를 리스트로 만들어 리스트 인덱스를 순서대로 돌려가며
O일 경우 count(누적 가점)을 1 증가시키고 그 가점을 score에 저장하며 X인 경우 count 를 0으로 만들고 score에 아무것도 저장하지 않도록 함.
주의하여야 할 점은 score 와 count 모두 한번의 테스트 케이스를 거치고 나면 초기화 시켜야 하기 때문에 새로운 테스트 케이스에
진입하기 전에 0점으로 초기화 시키도록 3~7번 라인 사이에 초기화를 넣어야 한다.
