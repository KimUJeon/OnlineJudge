import sys

now = 0
sun_list = []
moon_list = []
ds, ys = map(int, sys.stdin.readline().rstrip().split())
dm, ym = map(int, sys.stdin.readline().rstrip().split())
sun_time = now - ds
moon_time = now - dm


while True:
    if not sun_time < 0:
        sun_list.append(sun_time)
    if not moon_time < 0:
        moon_list.append(moon_time)
    if moon_time in sun_list:
        print(moon_time)
        break
    elif sun_time in moon_list:
        print(sun_time)
        break
    sun_time += ys
    moon_time += ym
