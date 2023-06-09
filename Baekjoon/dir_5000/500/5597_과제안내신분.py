import sys

submitters = []
students = [i for i in range(1, 31)]

for _ in range(28):
    submitters.append(sys.stdin.readline())

for submitter in submitters:
    students.remove(int(submitter))

print(students[0])
print(students[1])