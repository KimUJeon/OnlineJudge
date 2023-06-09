import sys

def dfs(depth, idx):
    global min_diff
    if depth == N//2:
        start, link = 0, 0
        for i in range(N):
            for j in range(N):
                if visit[i] and visit[j]:
                    start += _map[i][j]
                elif not visit[i] and not visit[j]:
                    link += _map[i][j]

        min_diff = min(min_diff, abs(start-link))
        return

    for i in range(idx, N):
        if not visit[i]:
            visit[i] = True
            dfs(depth+1, i+1)
            visit[i] = False

N = int(sys.stdin.readline())
_map = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(N)]
visit = [False] * N
min_diff = 1e9

dfs(0, 0)
print(min_diff)

'''
백트래킹의 무서움을 맛본 첫 문제... 열심히 공부해야 할 듯...
풀이를 설명하자면

1. 짝수 N 값을 입력받는다
2. _map 리스트 변수에 각 선수별 조합 점수를 입력 받는다
3. 선수 수 만큼 visit을 확인하는 리스트는 모두 False로 초기화 한다
4. min_diff(점수차)는 우선 가장 큰 수로 둔다 - 왜 1e9인지는 여러 블로그에 친절하게 설명됨
5. dfs 호출
5-1. 함수 내부에서 확인된 min_diff가 외부의 값을 수정할 수 있도록 전역 변수 선언
5-2. depth == 체크한 선수 로 생각하고 선수의 절반을 나누지 못하였다면 바로 for문으로 직행
5-3. for문에서 현재 idx 
'''