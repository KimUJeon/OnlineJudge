n = int(input())
c_score = 100
s_score = 100


for i in range(n):
    c, s = map(int, input().split())
    if c > s:
        s_score -= c
    elif c < s:
        c_score -= s
    else:
        pass
print(c_score)
print(s_score)

