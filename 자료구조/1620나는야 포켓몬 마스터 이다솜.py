N, M = map(int, input().split())

dogam1 = {}
dogam2 = {}

for i in range(1, N+1):
    pokemon = input()
    dogam1[i] = pokemon
    dogam2[pokemon] = i

for _ in range(M):
    solve = input()
    if solve.isdigit():
        print(dogam1[int(solve)])
    else:
        print(dogam2[solve])
