T = int(input())
A = 0
B = 0
C = 0

if T%10 != 0:
    print(-1)
else:
    if T < 300:
        B = T//60
        C = (T-60*B)//10
        print("%d %d %d"% (A, B, C))
    if T >= 300:
        A = T//300
        B = (T-300*A)//60
        C = (T-300*A-60*B)//10
        print("%d %d %d"%(A, B, C))
