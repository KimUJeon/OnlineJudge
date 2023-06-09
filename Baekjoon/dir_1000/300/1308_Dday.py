import sys

month_31 = [1, 3, 5, 7, 8, 10, 12]
s_year, s_month, s_day = map(int, sys.stdin.readline().rstrip().split())
e_year, e_month, e_day = map(int, sys.stdin.readline().rstrip().split())


def calc():
    count = 0
    n_year, n_month, n_day = s_year, s_month, s_day
    while True:
        if n_month in month_31:
            if n_day == 31:
                if n_month == 12:
                    n_year += 1
                    n_month = 1
                else:
                    n_month += 1
                n_day = 1
            else:
                n_day += 1
        elif n_month == 2 and ((n_year % 4 == 0 and n_year % 100 != 0) or n_year % 400 == 0):
            if n_day == 29:
                n_month = 3
                n_day = 1
            else:
                n_day += 1
        else:
            if n_month == 2:
                if n_day == 28:
                    n_month = 3
                    n_day = 1
                else:
                    n_day += 1
            else:
                if n_day == 30:
                    if n_month == 12:
                        n_year += 1
                        n_month = 1
                    else:
                        n_month += 1
                    n_day = 1
                else:
                    n_day += 1
        count += 1

        if n_year == e_year and n_month == e_month and n_day == e_day:
            print("D-{}".format(count))
            break

if e_year - s_year >= 1000:
    if e_year - s_year >= 1001:
        print("gg")
    elif e_month >= s_month:
        if e_month - s_month == 0:
            if e_day >= s_day:
                print("gg")
            else:
                calc()
        else:
            print("gg")
else:
    calc()

'''
생각해줘야 하는 조건이 생각보다 많은것 같았다... 라는 생각을 했는데 그냥 풀이할때
조건을 명확하게 하지 않아 반복적으로 틀린 것 같음
'''