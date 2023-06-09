T = input()

for i in range(int(T)):
    test_case = list(map(str, input().split()))
    P = ""
    S = list(test_case[1])

    for i in range(len(S)):
        string = S[i] * int(test_case[0])
        P += string
    i += 1
    print(P)


<문제>
문자열 S를 입력받은 후에, 각 문자를 R번 반복해 새 문자열 P를 만든 후 출력하는 프로그램을 작성하시오.
즉, 첫 번째 문자를 R번 반복하고, 두 번째 문자를 R번 반복하는 식으로 P를 만들면 된다.
S에는 QR Code "alphanumeric" 문자만 들어있다.
QR Code "alphanumeric" 문자는 0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ\$%*+-./: 이다.

<입력>
첫째 줄에 테스트 케이스의 개수 T(1 ≤ T ≤ 1,000)가 주어진다.
각 테스트 케이스는 반복 횟수 R(1 ≤ R ≤ 8), 문자열 S가 공백으로 구분되어 주어진다.
S의 길이는 적어도 1이며, 20글자를 넘지 않는다. 

2
3 ABC
5 /HTP

<출력>
각 테스트 케이스에 대해 P를 출력한다.
AAABBBCCC
/////HHHHHTTTTTPPPPP

<해설>
T 를 테스트 케이스의 개수로 정하고 T만큼 반복한다.
test_case 에 입력을 받아들임과 동시에 문자열로 지정하고
list(test_case[1]) 를 이용해 ABC와 같이 붙어있는 리스트를 또 리스트화 시켜
A B C로 분리한다. 이후 S의 길이에 따라 test_case[0] (반복횟수) 를 곱하여
미리 문자열을 빈칸으로 초기화 시켜둔 P에 더하는 방식으로 풀이하였다.
