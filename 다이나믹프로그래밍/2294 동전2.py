import sys
input = sys.stdin.readline

n, k = map(int, input().split())
num = []
for i in range(n):
    num.append(int(input()))

dp = [int(10e9)] * (k+1)
dp[0] = 0

for i in range(1, k+1):
    for n in num:
        if i - n >= 0:
            dp[i] = min(dp[i], dp[i-n] + 1)

print(dp[k] if dp[k] != int(10e9) else -1)