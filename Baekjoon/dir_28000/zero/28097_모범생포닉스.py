import sys

N = int(sys.stdin.readline().rstrip())
plans = map(int, sys.stdin.readline().rstrip().split())
tot_time = sum(plans) + ((N-1)*8)

print(f"{tot_time//24} {tot_time%24}")