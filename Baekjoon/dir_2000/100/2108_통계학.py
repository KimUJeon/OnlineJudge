import sys

N = int(sys.stdin.readline().rstrip())
nums = []
nums_count = dict()
for _ in range(N):
    num = int(sys.stdin.readline().rstrip())
    nums.append(num)
    if num in nums_count:
        nums_count[num] += 1
    else:
        nums_count[num] = 1
nums.sort()
nums_count = dict(sorted(nums_count.items(), key=lambda x: (x[1], x[0]), reverse=True))

print(round(sum(nums)/N))
print(nums[(N//2)])
nums_count = {key:value for key, value in nums_count.items() if value == nums_count[next(iter(nums_count))]}
nums_count = list(nums_count.items())
try:
    if nums_count[-1][1] == nums_count[-2][1]:
        print(nums_count[-2][0])
    else:
        print(nums_count[-1][0])
except:
    print(nums_count[0][0])

print(nums[-1]-nums[0])

'''
18번 라인의 nums_count[next(iter(nums_count))] 는 14번 라인에서 딕셔너리를 최빈값을 기준으로 내림차순 정렬을 했기 때문에
항상 맨 앞에 존재하는 value 값이 최빈값이기 때문에 이를 기준으로 잡기위해 iter()와 next()를 이용해 키 호출 후
값을 구하는 방식으로 구현하였고 18번 라인 전체 작동 방식은 첫번째 인덱스에 있는 딕셔너리의 Value와 동일하지 않으면
삭제하도록 함.


풀이에 1시간 좀 넘게 걸린듯. 그래도 완전히 내가 생각한 구조로 짜본거라 나름 뿌듯하다
'''