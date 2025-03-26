import sys
input = sys.stdin.readline

lst = list(map(int, input().split()))

# 스텝 인덱스, 왼발, 오른발
dp = [[[float('inf') for _ in range(5)] for _ in range(5)] for _ in range(len(lst) + 1)]
dp[0][0][0] = 0

def power(before, after):
    if before == after:
        return 1
    elif before == 0:
        return 2
    elif abs(after - before) % 2 == 0:
        return 4
    else:
        return 3
        
for i in range(1, len(lst)):
    target = lst[i-1]
    for left in range(5):
        for right in range(5):
            # 왼발
            dp[i][target][right] = min(dp[i][target][right], dp[i-1][left][right] + power(left, target))
            # 오른발
            dp[i][left][target] = min(dp[i][left][target], dp[i-1][left][right] + power(right, target))
            
result = float('inf')

for left in range(5):
    for right in range(5):
        result = min(result, dp[len(lst)-1][left][right])

print(result)