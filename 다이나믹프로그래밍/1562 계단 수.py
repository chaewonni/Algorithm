import sys
input = sys.stdin.readline

N = int(input())

# 딱 비트마스크만 추가
dp = [[[0] * (1 << 10) for _ in range(10)] for _ in range(N)]

for i in range(1, 10):
    dp[0][i][1 << i] = 1
    
for i in range(1, N):
    for j in range(10):
        for mask in range(1024):
            if j > 0:
                dp[i][j][mask | (1 << j)] += dp[i-1][j-1][mask]
            if j < 9:
                dp[i][j][mask | (1 << j)] += dp[i-1][j+1][mask]
                
sum = 0

for j in range(10):
    sum += dp[N-1][j][1023]
    
print(sum % 1000000000)