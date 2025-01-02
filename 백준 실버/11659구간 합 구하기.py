import sys
input = sys.stdin.readline

def solve():
    N, M = map(int, input().split())

    lst = [0] + list(map(int, input().split()))

    dp = [0] * (N+1)
    dp[0] = 0
    dp[1] = lst[1]

    for i in range(2, N+1):
        dp[i] = dp[i-1] + lst[i]

    for _ in range(M):
        a, b = map(int, input().split())
        print(dp[b]-dp[a-1])

solve()
