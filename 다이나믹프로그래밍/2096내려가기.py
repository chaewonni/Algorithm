import sys
input = sys.stdin.readline

N = int(input())

prev_max_dp = list(map(int, input().split()))
prev_min_dp = prev_max_dp[:]

for i in range(1, N):
    cnt = list(map(int, input().split()))
    
    # 현재 행의 최댓값
    cnt_max_dp = [
        cnt[0] + max(prev_max_dp[0], prev_max_dp[1]),
        cnt[1] + max(prev_max_dp[0], prev_max_dp[1], prev_max_dp[2]),
        cnt[2] + max(prev_max_dp[1], prev_max_dp[2])
    ]
    
    # 현재 행의 최솟값
    cnt_min_dp = [
        cnt[0] + min(prev_min_dp[0], prev_min_dp[1]),
        cnt[1] + min(prev_min_dp[0], prev_min_dp[1], prev_min_dp[2]),
        cnt[2] + min(prev_min_dp[1], prev_min_dp[2])
    ]
    
    prev_max_dp = cnt_max_dp
    prev_min_dp = cnt_min_dp
    
print(' '.join(map(str, [max(prev_max_dp), min(prev_min_dp)])))