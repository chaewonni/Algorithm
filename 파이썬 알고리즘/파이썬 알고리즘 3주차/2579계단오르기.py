n = int(input())

stairs = [0] * (n+1)
dp = [0] * (n+1)

for i in range(1, n+1):
    stairs[i] = int(input())


dp[1] = stairs[1]
if n >= 2:
    dp[2] = stairs[1] + stairs[2]
if n >= 3:
    dp[3] = stairs[3] + max(stairs[1], stairs[2])
    for i in range(4, n+1):
        dp[i] = stairs[i] + max(stairs[i-1] + dp[i-3], dp[i-2])

print(dp[n])