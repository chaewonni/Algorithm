import sys
input = sys.stdin.readline

N = int(input())

MOD = 1_000_000_000

dp = [[0]*10 for _ in range(N+1)]

for i in range(1, 10):
    dp[1][i] = 1

for i in range(2, N+1):
    for j in range(10):
        if j >= 9:
            dp[i][j] = dp[i-1][j-1]
        elif j < 1:
            dp[i][j] = dp[i-1][j+1]
        else:
            dp[i][j] = dp[i-1][j-1] + dp[i-1][j+1]
        dp[i][j] %= MOD

print(sum(dp[N]) % MOD)