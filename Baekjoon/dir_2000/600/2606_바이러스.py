import sys
from collections import deque

N = int(sys.stdin.readline().rstrip())
pair = int(sys.stdin.readline().rstrip())
max_val = max(N, pair)
network = [[] for _ in range(max_val+1)]
visit = [0 for _ in range(N+1)]


for _ in range(pair):
    pc = list(map(int, sys.stdin.readline().rstrip().split()))
    network[pc[0]-1].append(pc[1])
    network[pc[1]-1].append(pc[0])


def bfs():
    count = 0
    queue = deque([1])
    
    while queue:
        loc = queue.popleft()
        items = network[loc-1]
        
        for item in items:
            if not visit[item-1]:
                count += 1
                queue.append(item)
                visit[item-1] = 1

    if count == 0:
        print(0)
    else:
        print(count-1)

bfs()

'''
인덱스 에러만 3번이 떠서 구글링 해보며 비교를 해봤는데 로직 상으론 전혀 문제가 없었지만
가만 생각해보니 PC대수는 적더라도 서로 연결되어있는 PC 짝은 많을 수 있다는 생각이 들어 짝이 이루어지는 경우를
N대의 PC수나 짝을 이루는 pair 수 둘 중 큰 수를 적용하도록 수정함
'''