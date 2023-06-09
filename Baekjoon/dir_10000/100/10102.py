V = int(input())
votes = list(map(str, input()))

countA = votes.count('A')
countB = votes.count('B')

if countA == countB:
    print("Tie")
elif countA > countB:
    print('A')
else:
    print('B')
