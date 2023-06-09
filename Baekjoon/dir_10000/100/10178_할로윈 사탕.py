N = int(input())

for i in range(N):
    total, child = map(int, input().split())
    print("You get %d piece(s) and your dad gets %d piece(s)." %(total//child, total%child))