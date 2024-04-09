for a in range(2, 101):
    for b in range(2, 101):
        for c in range(b + 1, 101):
            for d in range(c + 1, 101):
                if pow(a, 3) == pow(b, 3) + pow(c, 3) + pow(d, 3):
                    print(f"Cube = {a}, Triple = ({b},{c},{d})")
                if pow(a, 3) < pow(b, 3) + pow(c, 3) + pow(d, 3):
                    break
