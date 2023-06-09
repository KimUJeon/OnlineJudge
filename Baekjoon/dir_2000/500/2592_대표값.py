num_list = []
count_list = []

for i in range(10):
    num_list.append(int(input()))

print(int(sum(num_list)/10))

num_list.sort()
set_list = list(set(num_list))

for i in range(len(set_list)):
    counted = num_list.count(set_list[i])
    count_list.append(counted)



print(set_list[count_list.index(max(count_list))])