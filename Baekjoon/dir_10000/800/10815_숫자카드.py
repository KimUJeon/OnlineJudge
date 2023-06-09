import sys

n = int(sys.stdin.readline().rstrip())
n_list = set(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline().rstrip())
m_list = list(map(int, sys.stdin.readline().split()))

# answer = {}

# for i in range(len(m_list)):
#     if m_list[i] in n_list:
#         answer[i] = '1'
#     else:
#         answer[i] = '0'

for i in m_list:
    if i in n_list:
        print(1, end=" ")
    else:
        print(0, end=" ")

# print(" ".join(answer))


'''
List 자료형에서 in 연산자의 시간 복잡도는 O(n) 이고
set이나 dict의 시간 복잡도는 O(1)로 해당 문제는 set이나 dict를 활용해
문제 풀이를 해야 하는 것으로 보인다. 따라서, 지금 문제와 같이 중복값이 없고
찾고자 하는 데이터의 유무를 파악하기 위해선 set을 사용하는 것이 바람직 하다고 볼 수 있다.
'''
