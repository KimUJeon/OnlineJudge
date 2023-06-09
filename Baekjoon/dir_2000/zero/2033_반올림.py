import sys

N = list(sys.stdin.readline().rstrip())
halfup = list(map(int, N[::-1]))

for i in range(len(N)-1):
    if i == len(halfup)-1:
        if halfup[i] >= 5:
            halfup[i] = 0
            halfup.append(1)
        break
    elif halfup[i] >= 5:
        halfup[i] = 0
        halfup[i+1] += 1
    elif halfup[i] < 5:
        halfup[i] = 0

halfup = list(map(str, halfup[::-1]))
print("".join(halfup))

'''
질문 게시판을 참고해 반례를 확인해가며 테스트해보았다
해당 문제의 가장 핵심 내용은 N의 자리수의 값이 들어올때 N-1 까지만 반올림을 해야 한다는 것 이다.
466이 500이 나오는 이유도 바로 그 때문, 십의 자리 까지만 반올림을 해야 하기 때문에 백의 자리에선 멈춤
'''