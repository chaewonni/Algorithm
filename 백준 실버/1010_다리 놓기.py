import sys
import math
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N, M = map(int, input().split())
    result = 1

    for i in range(N):
        result *= M
        M-=1

    result = result / math.factorial(N)

    print(int(result))