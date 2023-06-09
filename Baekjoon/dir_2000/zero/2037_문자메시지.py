import sys

phone = [['A', 'B', 'C'], ['D', 'E', 'F'],
         ['G', 'H', 'I'], ['J', 'K', 'L'], ['M', 'N', 'O'],
         ['P', 'Q', 'R', 'S'], ['T', 'U', 'V'], ['W', 'X', 'Y', 'Z']]

p, w = map(int, sys.stdin.readline().rstrip().split())
msg = sys.stdin.readline().rstrip()
total_time = 0

for i in range(len(msg)):
    if not i == 0:
        for j in range(len(phone)):
            if msg[i] in phone[j] and msg[i-1] in phone[j]:
                total_time += w + (phone[j].index(msg[i]) * p) + p
                break
            elif msg[i] == " ":
                total_time += p
                break
            elif msg[i] in phone[j]:
                total_time += (phone[j].index(msg[i]) * p) + p
                break
    else:
        for j in range(len(phone)):
            if msg[i] in phone[j]:
                total_time += (phone[j].index(msg[i]) * p) + p
                break

print(total_time)

'''
해당 문제의 조건은 다음과 같다
1. 입력 소모 시간 w, 중복 대기 시간 p
2. C를 입력하는 경우 A > +w B > +w C > +w 로 w*3 초가 소요된다
3. 이어서 B를 입력하는 경우 동일한 버튼에 문자가 있기 때문에 p 만큼 대기한 후 A > +w B > +w 로 p + w*2 초가 소요된다
4. 공백은 어떤 조건이던 간에 w 만 소모한다
'''