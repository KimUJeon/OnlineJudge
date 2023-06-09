S = input()
result = []


for asc in range(97, 123):
    counts = S.count(chr(asc))
    result.append(str(counts))

print(' '.join(result))