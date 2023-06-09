import sys

prize = int(sys.stdin.readline().rstrip())

print(int(prize*0.78), int(prize*0.8+(prize*0.2)*0.78))