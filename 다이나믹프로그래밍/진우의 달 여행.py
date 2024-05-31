import sys
input = sys.stdin.readline

N, M = map(int, input().split())

space = [list(map(int, input().split())) for _ in range(N)]
dp = [[[float('inf')] * 3 for _ in range(M)] for _ in range(N)]

#첫번째 행 초기화
for i in range(M):
    for j in range(3):
        dp[0][i][j] = space[0][i]

for i in range(1, N):
    for j in range(M):
        #오른쪽 이동
        if j < M-1:
            dp[i][j][0] = min(dp[i-1][j+1][1], dp[i-1][j+1][2]) + space[i][j]
        # 왼쪽 이동
        if 0 < j:
            dp[i][j][2] = min(dp[i-1][j-1][1], dp[i-1][j-1][0]) + space[i][j]
        # 아래쪽 이동
        dp[i][j][1] = min(dp[i-1][j][0], dp[i-1][j][2]) + space[i][j]

# 최종적인 최소 연료 소모량 계산
min_value = float('inf')
for row in dp[-1]:
    for each in row:
        min_value = min(min_value, each)

print(min_value)