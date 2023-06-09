pro_score = []
high_score = []

for _ in range(8):
    pro_score.append(int(input()))

revpro_score = list(reversed(sorted(pro_score)))
for i in range(5):
    high_score.append(str(pro_score.index(revpro_score[i])+1))

high_score.sort()

print(sum(revpro_score[:5]))
print(" ".join(high_score))

# pro_score - 각 문항별 점수, high_score - 점수 상위 5개 항목의 인덱스값
# revpro_score - sum 값을 쉽게 만들기 위해 정렬된 pro_score의 역순 리스트