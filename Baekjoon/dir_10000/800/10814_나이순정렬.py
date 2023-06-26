import sys

N = int(sys.stdin.readline().rstrip())
students = []
for i in range(N):
    age, name = map(str, input().split())
    age = int(age)
    students.append((age, name))
students = sorted(students, key = lambda x : (x[0]))

for i in range(N):
    print(students[i][0], students[i][1])