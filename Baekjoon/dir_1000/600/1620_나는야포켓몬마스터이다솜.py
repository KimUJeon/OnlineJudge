import sys

N, M = map(int, sys.stdin.readline().rstrip().split())
pokemons = dict()
for idx in range(1, N + 1):
    pokemon = sys.stdin.readline().rstrip()
    pokemons[idx] = pokemon
    pokemons[pokemon] = idx


for _ in range(M):
    question = sys.stdin.readline().rstrip()
    if 48 <= ord(question[0]) <= 57:
        print(pokemons[int(question)])
    else:
        print(pokemons[question])
