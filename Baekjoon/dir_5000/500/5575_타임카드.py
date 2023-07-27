import sys

people = []
for _ in range(3):
    people.append(list(map(int, sys.stdin.readline().rstrip().split())))

for items in people:
    start = items[0] * 3600 + items[1] * 60 + items[2]
    end = items[3] * 3600 + items[4] * 60 + items[5]
    cal_time = end - start

    res_hr = cal_time//3600
    cal_time -= 3600 * res_hr
    res_min = cal_time//60
    cal_time -= 60 * res_min

    print(res_hr, res_min, cal_time)