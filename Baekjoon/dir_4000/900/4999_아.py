import sys

jaehwan = sys.stdin.readline()
doc = sys.stdin.readline()

if jaehwan.count('a') >= doc.count('a'):
    print("go")
else:
    print("no")