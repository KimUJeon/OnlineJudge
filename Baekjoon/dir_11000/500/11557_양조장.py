T = int(input())

for i in range(T):
    school_sobi = {}
    N = int(input())
    for j in range(N):
        school, amount = input().split()
        school_sobi[school] = int(amount)
    max_key = max(school_sobi, key=school_sobi.get)
    print(max_key)
