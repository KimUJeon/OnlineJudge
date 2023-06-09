M = int(input())
N = int(input())

nat_num = 0
result = []

for i in range(0, 101):
    nat_num = pow(i, 2)
    if(M <= nat_num <= N):
        result.append(nat_num)
    elif(nat_num > N):
        break

if len(result) == 0:
    print(-1)

else:
    sum_all = sum(result)
    print(sum_all)
    print(result[0])

