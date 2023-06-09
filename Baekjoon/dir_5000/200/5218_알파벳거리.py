T = int(input())

for _ in range(T):
    result = []
    origin, change = input().split()
    for i in range(len(origin)):
       asc_ori = ord(origin[i]) - 64
       asc_cha = ord(change[i]) - 64
       if asc_ori > asc_cha:
           result.append(str((asc_cha - asc_ori) + 26))
       else:
           result.append(str(asc_cha - asc_ori))

    print("Distances:", ' '.join(result))