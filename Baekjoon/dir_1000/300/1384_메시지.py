import sys

group_num = 1

while True:
    n = int(sys.stdin.readline().rstrip())
    order_list = []
    people = []
    if n == 0:
        break

    for i in range(n):
        write = list(map(str, sys.stdin.readline().rstrip().split()))
        order_list.append(write)

    for p_idx, order in enumerate(order_list):
        person = order[0]
        for idx, word in enumerate(order[1:]):
            if word == "N":
                idx_gap = p_idx - (idx + 1)
                if idx_gap < 0:
                    people.append([order_list[idx_gap + len(order_list)][0], person])
                else:
                    people.append([order_list[idx_gap][0], person])

    print(f"Group {group_num}")
    if people:
        for result in people:
            print(f"{result[0]} was nasty about {result[1]}")
    else:
        print("Nobody was nasty")
    print()

    group_num += 1
