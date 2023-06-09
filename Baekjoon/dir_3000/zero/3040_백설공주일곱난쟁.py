# dwarf = []
#
# for _ in range(9):
#     dwarf.append(int(input()))
#
# for i in range(9):
#     for j in range(i+1, 9):
#         if sum(dwarf) - (dwarf[i]+dwarf[j]) == 100:
#             dwarf.remove(dwarf[i])
#             dwarf.remove(dwarf[j])
#             break
#
# for k in range(len(dwarf)):
#     print(dwarf[k])

dwarf = []
for _ in range(9):
    dwarf.append(int(input()))
for i in range(9):
    for j in range(i+1, 9):
        result = sum(dwarf) - (dwarf[i] + dwarf[j])
        if result == 100:
            for k in range(9):
                if k == i or k == j:
                    continue
                else:
                    print(dwarf[k])

# 왜 내가 작성한 코드는 ValueError가 뜨는지 모르겠음
# 출력이나 타입은 분명 이상이 없음