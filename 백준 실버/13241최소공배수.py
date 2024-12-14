import math

def solve():
    A, B = map(int, input().split())

    gcd = math.gcd(A,B)

    print(A*B // gcd)

solve()