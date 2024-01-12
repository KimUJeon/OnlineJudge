import sys

start_time = list(map(int, sys.stdin.readline().rstrip().split(":")))
end_time = list(map(int, sys.stdin.readline().rstrip().split(":")))

start_sec = start_time[0]*3600 + start_time[1]*60 + start_time[2]
end_sec = end_time[0]*3600 + end_time[1]*60 + end_time[2]

if start_sec > end_sec:
    print(end_sec-start_sec+3600*24)
else:
    print(end_sec-start_sec)