alpha = input()
alpha_list = []

alpha = alpha.lower()

for word in range(ord('a'), ord('z')+1):
    alpha_list.append(alpha.count(chr(word)))

max_num = max(alpha_list)

other = alpha_list.count(max_num)
if other >= 2:
    print("?")
else:
    pos = int(alpha_list.index(max_num))
    print(chr(pos+97).upper())



<문제>
알파벳 대소문자로 된 단어가 주어지면, 이 단어에서 가장 많이 사용된 알파벳이
무엇인지 알아내는 프로그램을 작성하시오. 단, 대문자와 소문자를 구분하지 않는다.

<입력>
첫째 줄에 알파벳 대소문자로 이루어진 단어가 주어진다. 주어지는 단어의 길이는 1,000,000을 넘지 않는다.
ex.1) Mississipi
ex.2) zZa

<출력>
첫째 줄에 이 단어에서 가장 많이 사용된 알파벳을 대문자로 출력한다. 단, 가장 많이 사용된 알파벳이 여러 개 존재하는 경우에는 ?를 출력한다.
ex.1) ?
ex.2) Z

<해설>
alpha를 입력받는 단어로 지정하고 추후에 알파벳들을 분리하기 위해 alpha_list 를 빈 리스트로 초기화 시켰다.
조건에 "대소문자를 구분하지 않는다" 가 있으므로 lower() 함수를 통해 모두 소문자로 만든뒤
for 문에서 ord(). 즉, 아스키코드 를 이용한 반복문을 실행해 a - z 까지 각 알파벳의 갯수를 alpha_list 에
순서대로 추가하였다.
max_num 은 alpha_list 에서 가장 큰 숫자를 저장해 두는 변수로 바로 다음 라인에 오는 ohter 에서 많이 사용된
알파벳이 2개 이상인지 확인하는 용도로 사용이 되었다.
