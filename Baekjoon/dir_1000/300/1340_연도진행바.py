import sys

months = {
    "January": 31,
    "February": 28,
    "March": 31,
    "April": 30,
    "May": 31,
    "June": 30,
    "July": 31,
    "August": 31,
    "September": 30,
    "October": 31,
    "November": 30,
    "December": 31,
}
calc_time = 0
i_month, i_day, i_year, i_time = map(str, sys.stdin.readline().rstrip().split())

if int(i_year) % 400 == 0 or (int(i_year) % 4 == 0 and int(i_year) % 100 != 0):
    total_time = 366 * 24 * 60
    for key, value in months.items():
        if key == i_month:
            break
        calc_time += value
        if key == "February":
            calc_time += 1

    # 일 => 분 단위로 변경
    calc_time = (
        (calc_time + int(i_day[:2])) * 24 * 60
        + int(i_time[:2]) * 60
        + int(i_time[-2:])
        - 1440
    )

else:
    total_time = 365 * 24 * 60
    for key, value in months.items():
        if key == i_month:
            break
        calc_time += value

    calc_time = (
        (calc_time + int(i_day[:2])) * 24 * 60
        + int(i_time[:2]) * 60
        + int(i_time[-2:])
        - 1440
    )

print(calc_time / total_time * 100)
