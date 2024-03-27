import sys, math
from itertools import combinations_with_replacement

n = int(sys.stdin.readline().rstrip())
sq_num = [i**2 for i in range(1, int(math.sqrt(n)) + 1)]
sq_num_2 = [sum(j) for j in combinations_with_replacement(sq_num, 2)]
flag = True

if n in sq_num:
    flag = False
    print(1)
elif n in sq_num_2:
    flag = False
    print(2)
else:
    # 두 제곱 + 한 제곱인 경우 3개를 사용하였기 때문에 다음과 같이 작성함
    for sq in sq_num:
        if n - sq in sq_num_2:
            flag = False
            print(3)
            break
if flag:
    print(4)
