people = []

for _ in range(9):
    people.append(int(input()))

people.sort()

for i in people:
    for j in people:
        if 100 == sum(people) -(i+j):
            people.remove(i)
            people.remove(j)
            break

for k in people:
    print(k)