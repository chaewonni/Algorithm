N, M = map(int, input().split())

basket=[]

for i in range(0, N+1):
    basket.append(i)

for i in range(M):
    s1, s2 = map(int, input().split())

    while(s1 < s2):
        basket[s1], basket[s2] = basket[s2], basket[s1]
        s1 += 1
        s2 -= 1

for i in range(1, N+1):
    print(basket[i], end=' ')