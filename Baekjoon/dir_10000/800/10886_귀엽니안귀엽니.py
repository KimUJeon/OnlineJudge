N = int(input())
count = 0

for i in range(N):
    answer = int(input())
    if answer == 1:
        count += 1
    else:
        continue

if count > N/2:
    print("Junhee is cute!")
else:
    print("Junhee is not cute!")
