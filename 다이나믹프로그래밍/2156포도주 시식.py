n = int(input())

# 포도주 잔에 들어있는 포도주의 양을 저장할 리스트
s_list = []

for _ in range(n):
    s_list.append(int(input()))

dp = [[0] * 3 for _ in range(n)]

# 각 포도주 잔에 대해 가능한 모든 상태를 계산
for i in range(0, n):
    if i == 0:
        # 첫 번째 잔을 처리하는 경우의 초기 설정
        dp[i][0] = s_list[0]  # 첫 번째 잔을 마심
        dp[i][1] = 0          # 불가능한 상태
        dp[i][2] = s_list[0]  # 첫 번째 잔을 마심
    elif i == 1:
        # 두 번째 잔을 처리하는 경우의 초기 설정
        dp[i][0] = s_list[0]             # 첫 번째 잔만 마심
        dp[i][1] = s_list[0] + s_list[1] # 첫 번째와 두 번째 잔을 마심
        dp[i][2] = s_list[1]             # 두 번째 잔만 마심
    else:
        # 세 번째 잔 이후부터는 점화식에 따라 계산
        dp[i][0] = dp[i-1][1]            # i-1번째 잔을 마시고 i번째 잔을 마시지 않음
        dp[i][1] = dp[i-1][2] + s_list[i] # i-1번째 잔을 마시지 않고, i번째 잔을 마심
        dp[i][2] = dp[i-1][0] + s_list[i] # i-2번째까지의 최대값과 i번째 잔을 마심

# 마지막 잔까지 고려했을 때의 최대 포도주 양을 출력
print(max(dp[n-1]))