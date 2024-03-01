from itertools import permutations

K, M = map(int, input().split())

primes = list(range(100000))
#아리스토테네스의 체
for i in range(2, int(len(primes) ** 0.5) + 1):
    if primes[i]:
        # for j in range(j*2, len(range), i):
        #     primes[j] = 0
        #리스트 슬라이싱
        primes[i * i :: i] = [0] * len(primes[i * i :: i])
primes = set(filter(None, primes[2:]))

c1, c2 = set(), set()

for num in permutations("0123456789", K):
    N = "".join(num)
    if N.startswith("0"):
        continue
    N = int(N)

    # for i in range(2, int(N/2) + 1):
    #     if i in primes and N-i in primes:
    #         if i != N-i:
    #             c1.add(N)
    #             break

    if (N != 4 and N - 2 in primes) or (N > 7 and N % 2 == 0):
        c1.add(N)

    mul = N
    while mul % M == 0:
        mul //= M

    for i in range(2, int(mul ** 0.5) + 1):
        if mul % i == 0:
            if i in primes and mul // i in primes:
                c2.add(N)
            break

print(len(c1&c2))