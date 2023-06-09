N = int(input())

for i in range(1, N+1):
    print(" " * (N-i) + "*" * i)
    if i == N:
        for j in range(1, N):
            print(" " * j + "*" * (N-j))



'''
출력 예시

  *
 **
***
 **
  *
'''