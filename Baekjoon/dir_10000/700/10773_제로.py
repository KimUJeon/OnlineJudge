K = int(input())
save_num = []

for _ in range(K):
    num = int(input())
    if num == 0:
        save_num.pop()
    else:
        save_num.append(num)

print(sum(save_num))