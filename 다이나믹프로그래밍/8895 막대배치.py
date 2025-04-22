import sys
input = sys.stdin.readline

dp = [[[0 for _ in range(21)] for _ in range(21)] for _ in range(21)]
dp[1][1][1] = 1

for n in range(2, 21):
    for l in range(n+1):
        for r in range(n+1):
            dp[n][l][r] = dp[n-1][l-1][r] + dp[n-1][l][r-1] + dp[n-1][l][r] * (n-2)

t = int(sys.stdin.readline())
for _ in range(t):
    n, l, r = map(int,sys.stdin.readline().split())
    print(dp[n][l][r])