import sys
input = sys.stdin.readline

N = int(input())
num = list(map(int, input().split()))

INF = float('inf')
dp = [INF] * N

dp[0] = 0

for i in range(N-1):
    for j in range(1, num[i] + 1):
        if i+j < N:
            if dp[i+j] == INF:
                dp[i+j] = dp[i] + 1 
          
print(dp)

if dp[N-1] == INF:
    print(-1)
else:
    print(dp[N-1])