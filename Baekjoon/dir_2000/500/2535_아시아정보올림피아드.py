import sys

N = int(sys.stdin.readline().rstrip())
people = []
cnt = 0
country = {}
result = []

for _ in range(N):
    people.append(list(map(int, sys.stdin.readline().rstrip().split())))
people.sort(key=lambda x: x[2], reverse=True)

for person in people:
    if person[0] not in country:
        country[person[0]] = 1
        result.append(person[:2])
        cnt += 1
    elif person[0] in country:
        if country[person[0]] < 2:
            country[person[0]] += 1
            result.append(person[:2])
            cnt += 1

    if cnt == 3:
        break

for item in result:
    print(item[0], item[1])
