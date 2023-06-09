A, B = map(int, input().split())
count = 0
count_list = []

for i in range(1, B+1):
    count += i
    for j in range(i):
        count_list.append(int(i))
    if count > B:
        break

count_list = count_list[A-1:B]
print(sum(count_list))