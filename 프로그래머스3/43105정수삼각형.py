def solution(triangle):
    answer = 0
    
    dp = [[0] * len(triangle[-1]) for _ in range(len(triangle))]
    
    for i in range(len(triangle)):        #0  1   2    3     4
        for j in range(len(triangle[i])): #0 01 012 0123 01234 
            if i == 0 and j == 0:
                dp[i][j] = triangle[i][j]
            elif j > 0 and j < i:
                dp[i][j] = max(dp[i-1][j-1], dp[i-1][j]) + triangle[i][j]
            elif j == 0:
                dp[i][j] = dp[i-1][j] + triangle[i][j]
            elif j == i:
                dp[i][j] = dp[i-1][j-1] + triangle[i][j]
                
            
    return max(dp[len(triangle)-1])